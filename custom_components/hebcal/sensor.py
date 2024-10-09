"""
Platform to get Hebcal Times And Hebcalh information for Home Assistant.
"""
import codecs
import aiofiles
import datetime
import json
import logging
import pathlib
import time
import re
import aiohttp
import homeassistant.helpers.config_validation as cv
import pytz
import voluptuous as vol
from aiozoneinfo import async_get_time_zone
from homeassistant.components.sensor import ENTITY_ID_FORMAT
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_LATITUDE, CONF_LONGITUDE, CONF_TIME_ZONE, CONF_RESOURCES
from homeassistant.core import callback
from homeassistant.helpers.entity import Entity, async_generate_entity_id
from homeassistant.helpers.sun import get_astral_event_date

from .const import (
    HAVDALAH_MINUTES,
    PLATFORM_FOLDER,
    SENSOR_PREFIX,
    SENSOR_TYPES,
    TIME_AFTER_CHECK,
    TIME_BEFORE_CHECK,
    JERUSALEM_CANDLE,
    TZEIT_HAKOCHAVIM,
    OMER_COUNT_TYPE,
    DEFAULT_HAVDALAH_MINUTES,
    DEFAULT_TIME_BEFORE_CHECK,
    DEFAULT_TIME_AFTER_CHECK,
    DEFAULT_JERUSALEM_CANDLE,
    DEFAULT_TZEIT_HAKOCHAVIM,
    DEFAULT_OMER_COUNT_TYPE,
    OMER_DAYS,
    HEBREW_WEEKDAY,
    HEBCAL_DATE_URL,
    HEBCAL_DATE_URL_HAVDALAH,
    HEBCAL_CONVERTER_URL,
    LANGUAGE,
    DEFAULT_LANGUAGE,
    LANGUAGE_DATA,
    HEBCAL_ZMANIM_URL,
)

_LOGGER = logging.getLogger(__name__)

version = "2.5.1"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_LATITUDE): cv.latitude,
        vol.Optional(CONF_LONGITUDE): cv.longitude,
        vol.Optional(CONF_TIME_ZONE): cv.string,
        vol.Optional(HAVDALAH_MINUTES, default=DEFAULT_HAVDALAH_MINUTES): cv.positive_int,
        vol.Optional(TIME_BEFORE_CHECK, default=DEFAULT_TIME_BEFORE_CHECK): cv.positive_int,
        vol.Optional(TIME_AFTER_CHECK, default=DEFAULT_TIME_AFTER_CHECK): cv.positive_int,
        vol.Optional(JERUSALEM_CANDLE, default=DEFAULT_JERUSALEM_CANDLE): cv.boolean,
        vol.Optional(TZEIT_HAKOCHAVIM, default=DEFAULT_TZEIT_HAKOCHAVIM): cv.boolean,
        vol.Optional(OMER_COUNT_TYPE, default=DEFAULT_OMER_COUNT_TYPE): cv.positive_int,
        vol.Optional(LANGUAGE, default=DEFAULT_LANGUAGE): cv.string,
        vol.Optional(
            CONF_RESOURCES,
            default=[
                "shabbat_in",
                "shabbat_out",
                "parasha",
                "hebrew_date",
                "is_shabbat",
                "yomtov_in",
                "yomtov_out",
                "is_yomtov",
                "yomtov_name",
                "omer_day",
                "event_name",
                "zmanim",
            ],
        ): vol.All(cv.ensure_list, [vol.In(SENSOR_TYPES)]),
    }
)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Hebcal config sensors."""
    latitude = config.get(CONF_LATITUDE, hass.config.latitude)
    longitude = config.get(CONF_LONGITUDE, hass.config.longitude)
    timezone = config.get(CONF_TIME_ZONE, hass.config.time_zone)
    havdalah = config.get(HAVDALAH_MINUTES)
    time_before = config.get(TIME_BEFORE_CHECK)
    time_after = config.get(TIME_AFTER_CHECK)
    jerusalem_candle = config.get(JERUSALEM_CANDLE)
    tzeit_hakochavim = config.get(TZEIT_HAKOCHAVIM)
    omer_count_type = config.get(OMER_COUNT_TYPE)
    language = config.get(LANGUAGE)

    if None in (latitude, longitude, timezone):
        _LOGGER.error("Latitude or Longitude or TimeZone are not set in Home Assistant config")
        return

    entities = []

    for resource in config[CONF_RESOURCES]:
        sensor_type = resource.lower()
        if sensor_type not in SENSOR_TYPES:
            SENSOR_TYPES[sensor_type] = [sensor_type.title(), "", "mdi:flash"]
        entities.append(
            Hebcal(
                hass,
                sensor_type,
                timezone,
                latitude,
                longitude,
                havdalah,
                time_before,
                time_after,
                jerusalem_candle,
                tzeit_hakochavim,
                omer_count_type,
                language,
            )
        )

    async_add_entities(entities, False)


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


class Hebcal(Entity):
    """Create Hebcal sensor."""

    hebcal_db = []
    temp_data = []
    shabbat_in = None
    shabbat_out = None
    yomtov_in = None
    yomtov_out = None
    file_time_stamp = None
    start = None
    end = None
    config_path = None
    candle = 18

    def __init__(
            self,
            hass,
            sensor_type,
            timezone,
            latitude,
            longitude,
            havdalah,
            time_before,
            time_after,
            jerusalem_candle,
            tzeit_hakochavim,
            omer_count_type,
            language,

    ):
        """Initialize the sensor"""
        self.type = sensor_type
        self.entity_id = async_generate_entity_id(
            ENTITY_ID_FORMAT,
            "_".join([SENSOR_PREFIX, SENSOR_TYPES[self.type][2]]),
            hass=hass,
        )
        self._latitude = latitude
        self._longitude = longitude
        self._timezone = timezone
        self._havdalah = havdalah
        self._time_before = time_before
        self._time_after = time_after
        self._jerusalem_candle = jerusalem_candle
        self._tzeit_hakochavim = tzeit_hakochavim
        self._omer_count_type = omer_count_type
        self._language = language
        self.config_path = hass.config.path() + PLATFORM_FOLDER
        self._state = None
        self.parashat = None
        self.yomtov_name = None
        self.rosh_hashana = False
        self.holiday_count = 0
        self.omer = False
        self.hanucka = False
        self.zmanim = {}
        self.local_timezone = None
        # await self.create_db_file()

    @property
    def name(self) -> str:
        """Return the name of the sensor"""
        if self._language == "hebrew":
            return SENSOR_TYPES[self.type][0]
        return SENSOR_TYPES[self.type][2]

    @property
    def icon(self):
        """Icon to use in the frontend"""
        return SENSOR_TYPES[self.type][1]

    @property
    def should_poll(self) -> bool:
        """Return true if the device should be polled for state updates"""
        return True

    @property
    def state(self):
        """Return the state of the sensor"""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        if self.type != "zmanim":
            return {}
        return self.zmanim

    async def async_update(self):
        """Update our sensor state"""
        if not (pathlib.Path(self.config_path + "hebcal_data.json").is_file()):
            await self.create_db_file()
        elif not self.hebcal_db or self.file_time_stamp is None:
            await self.create_db_file()
        elif self.file_time_stamp != datetime.date.today() or len(self.hebcal_db) <= 2:
            await self.create_db_file()
        type_to_func = {
            "shabbat_in": self.get_shabbat_time_in,
            "shabbat_out": self.get_shabbat_time_out,
            "is_shabbat": self.is_shabbat,
            "parasha": self.get_parasha,
            "yomtov_in": self.get_yomtov_time_in,
            "yomtov_out": self.get_yomtov_time_out,
            "is_yomtov": self.is_yomtov,
            "yomtov_name": self.get_yomtov_name,
            "event_name": self.get_event_name,
            "omer_day": self.get_omer_day,
            "hebrew_date": self.get_hebrew_date,
            "zmanim": self.get_zmanim,
        }
        self._state = await type_to_func[self.type]()
        self.async_write_ha_state()

    async def create_db_file(self):
        """Create a json db"""
        self.shabbat_in = None
        self.shabbat_out = None
        self.yomtov_in = None
        self.yomtov_out = None
        self.parashat = None
        self.set_days()
        self.temp_data = []
        self.file_time_stamp = datetime.date.today()
        self.temp_data.append({"update_date": str(self.file_time_stamp)})
        await self.set_local_timezone()
        if self._jerusalem_candle:
            self.candle = 40
        try:
            h_url = HEBCAL_DATE_URL.format(str(LANGUAGE_DATA[self._language][-1]), str(self.start), str(self.end),
                                           str(self._latitude), str(self._longitude),
                                           str(self._timezone), str(self.candle))
            if not self._tzeit_hakochavim:
                h_url = HEBCAL_DATE_URL_HAVDALAH.format(str(LANGUAGE_DATA[self._language][-1]), str(self.start),
                                                        str(self.end), str(self._latitude),
                                                        str(self._longitude), str(self._timezone), str(self._havdalah),
                                                        str(self.candle))
            async with aiohttp.ClientSession() as session:
                html = await fetch(
                    session, h_url, )
                temp_db = json.loads(html)
                html = await fetch(
                    session, HEBCAL_ZMANIM_URL.format(str(self._latitude), str(self._longitude),
                                                      str(self._timezone), str(self.file_time_stamp)), )
                zmanim_temp = json.loads(html)['times']
                zmanim_temp.update({'title': 'day_zmanim'})
                temp_db['items'].append(zmanim_temp)
                async with aiofiles.open(
                        self.config_path + "hebcal_data_full.json", "w", encoding="utf-8"
                ) as outfile:
                    temp_data = json.dumps(temp_db, skipkeys=False, ensure_ascii=False, indent=4, separators=None,
                                           default=None, sort_keys=True)
                    await outfile.write(temp_data)
                await self.filter_db(temp_db["items"], "new")
            async with aiohttp.ClientSession() as session:
                html = await fetch(
                    session, HEBCAL_CONVERTER_URL.format(self.file_time_stamp.year, self.file_time_stamp.month,
                                                         self.file_time_stamp.day), )
                html = await self.add_english_date(html)
                self.temp_data.append(html)

        except Exception as e:
            _LOGGER.error("Error while create DB: %s. Restore From Backup", str(e))
            async with aiofiles.open(
                    self.config_path + "hebcal_data.json", encoding="utf-8"
            ) as data_file:
                temp_data_db = await data_file.read()
                self.hebcal_db = json.loads(temp_data_db)
                await self.filter_db(self.hebcal_db, "update")
            self.file_time_stamp = datetime.datetime.strptime(
                self.hebcal_db[0]["update_date"], "%Y-%m-%d"
            ).date()
        if len(self.temp_data) > 2:
            self.hebcal_db = self.temp_data
            async with aiofiles.open(
                    self.config_path + "hebcal_data.json", "w", encoding="utf-8"
            ) as outfile:
                temp_data = json.dumps(self.hebcal_db, skipkeys=False, ensure_ascii=False, indent=4, separators=None,
                                       default=None, sort_keys=True)
                await outfile.write(temp_data)

    async def filter_db(self, temp_db, state):
        """Filters the database"""
        special_holiday = False
        if state == "new":
            for extract_data in temp_db:
                if "major" in list(extract_data.values()):
                    self.rosh_hashana = (
                        True if any("Rosh Hashana" in str(value) for value in extract_data.values()) else False)
                if "date" in extract_data:
                    extract_data["date"] = (
                        extract_data["date"][:19]
                    )
                if "candles" in list(extract_data.values()):
                    is_in = datetime.datetime.strptime(
                        extract_data["date"], "%Y-%m-%dT%H:%M:%S"
                    )
                    if self.check_candles_time(is_in):
                        if is_in.isoweekday() == 5:
                            self.shabbat_in = is_in
                            self.temp_data.append(extract_data)
                        elif is_in.isoweekday() != 6 and is_in.isoweekday() != 5:
                            self.holiday_count += 1
                            self.yomtov_in = is_in
                            self.temp_data.append(extract_data)
                    elif is_in.isoweekday() == 6:
                        special_holiday = True
                if "havdalah" in list(extract_data.values()):
                    is_out = datetime.datetime.strptime(
                        extract_data["date"], "%Y-%m-%dT%H:%M:%S"
                    )
                    if is_out.isoweekday() == 6:
                        self.shabbat_out = is_out
                        self.temp_data.append(extract_data)
                    elif is_out.isoweekday() < 5 or is_out.isoweekday() > 6:
                        self.yomtov_out = is_out
                        self.temp_data.append(extract_data)
                if "parashat" in list(extract_data.values()):
                    self.parashat = extract_data["title"]
                    self.temp_data.append(extract_data)
                if "day_zmanim" in list(extract_data.values()):
                    for x in LANGUAGE_DATA[self._language][4]:
                        self.zmanim.update({LANGUAGE_DATA[self._language][4][x]: extract_data[x][11:16]})
                    self.zmanim.update({'title': 'day_zmanim'})
                    self.temp_data.append(self.zmanim)
                    # self.zmanim.pop('title')
                if any(
                        x in ["yomtov", "holiday", "omer", "roshchodesh"]
                        for x in list(extract_data.values())):
                    extract_data["start"] = self.sunset_time(extract_data["date"], -1)
                    extract_data["end"] = self.sunset_time(extract_data["date"], 0)
                    self.temp_data.append(extract_data)
            if self.shabbat_in and not self.shabbat_out:
                self.shabbat_out = (
                        self.shabbat_in
                        + datetime.timedelta(days=1)
                        + datetime.timedelta(minutes=60)
                )
                self.temp_data.append(
                    {
                        "hebrew": "הבדלה - 42 דקות",
                        "date": str(self.shabbat_out).replace(" ", "T"),
                        "className": "havdalah",
                        "allDay": False,
                        "title": "הבדלה - ידני",
                    }
                )
                if special_holiday:
                    self.yomtov_in = (
                            self.shabbat_in
                            + datetime.timedelta(days=1)
                    )
                    self.temp_data.append(
                        {
                            "className": "candles",
                            "hebrew": "הדלקת נרות",
                            "date": str(self.yomtov_in).replace(" ", "T"),
                            "allDay": False,
                            "title": "הדלקת נרות - ידני",
                        }
                    )
            elif not self.shabbat_in and self.shabbat_out:
                self.shabbat_in = (
                        self.shabbat_out
                        - datetime.timedelta(days=1)
                        - datetime.timedelta(minutes=60)
                )
                self.temp_data.append(
                    {
                        "className": "candles",
                        "hebrew": "הדלקת נרות",
                        "date": str(self.shabbat_in).replace(" ", "T"),
                        "allDay": False,
                        "title": "הדלקת נרות - ידני",
                    }
                )
            if self.yomtov_in and not self.yomtov_out:
                if self.rosh_hashana:
                    self.yomtov_out = (
                            self.yomtov_in
                            + datetime.timedelta(days=2)
                            + datetime.timedelta(minutes=60)
                    )
                else:
                    self.yomtov_out = (
                            self.yomtov_in
                            + datetime.timedelta(days=1)
                            + datetime.timedelta(minutes=60)
                    )
                self.temp_data.append(
                    {
                        "hebrew": "הבדלה - 42 דקות",
                        "date": str(self.yomtov_out).replace(" ", "T"),
                        "className": "havdalah",
                        "allDay": False,
                        "title": "הבדלה - ידני",
                    }
                )
            elif not self.yomtov_in and self.yomtov_out:
                self.yomtov_in = (
                        self.yomtov_out
                        - datetime.timedelta(days=1)
                        - datetime.timedelta(minutes=60)
                )
                self.temp_data.append(
                    {
                        "className": "candles",
                        "hebrew": "הדלקת נרות",
                        "date": str(self.yomtov_in).replace(" ", "T"),
                        "allDay": False,
                        "title": "הדלקת נרות - ידני",
                    }
                )
        elif state == "update":
            for extract_data in temp_db:
                if "date" in extract_data:
                    extract_data["date"] = (
                        extract_data["date"][:19]
                    )
                if "candles" in list(extract_data.values()):
                    is_in = datetime.datetime.strptime(
                        extract_data["date"], "%Y-%m-%dT%H:%M:%S"
                    )
                    if is_in.isoweekday() == 5:
                        self.shabbat_in = is_in
                    elif is_in.isoweekday() != 5:
                        self.yomtov_in = is_in
                if "havdalah" in list(extract_data.values()):
                    is_out = datetime.datetime.strptime(
                        extract_data["date"], "%Y-%m-%dT%H:%M:%S"
                    )
                    if is_out.isoweekday() == 6:
                        self.shabbat_out = is_out
                    elif is_out.isoweekday() < 5 or is_out.isoweekday() > 6:
                        self.yomtov_out = is_out
                if "parashat" in list(extract_data.values()):
                    self.parashat = extract_data["title"]
                if "day_zmanim" in list(extract_data.values()):
                    self.zmanim = extract_data
                    self.zmanim.pop('title')

    async def add_english_date(self, data):
        temp = json.loads(data)
        english_date = str(temp["hd"]) + " " + str(temp["hm"]) + " " + str(temp["hy"])
        temp["english"] = english_date
        return temp

    @callback
    def check_candles_time(self, candles):
        sunset = datetime.datetime.strptime(self.sunset_time(str(candles)[:10], 0)
                                            , "%Y-%m-%dT%H:%M:%S")
        return sunset > candles

    @callback
    def sunset_time(self, date, day):
        date = datetime.datetime.strptime(date[:10], '%Y-%m-%d').date() + datetime.timedelta(days=day)
        data = get_astral_event_date(self.hass, event="sunset", date=date)
        sunset = self.utc_to_local(data, self.local_timezone)
        # _LOGGER.error(sunset)
        return str(sunset)[:19].replace(" ", "T")

    @callback
    def set_days(self):
        """Set the friday and saturday."""
        weekday = self.set_sunday(datetime.date.today().isoweekday())
        self.start = datetime.date.today() + datetime.timedelta(days=weekday)
        self.end = datetime.date.today() + datetime.timedelta(
            days=weekday + 6)

    @classmethod
    def set_sunday(cls, day):
        """Set friday day."""
        switcher = {
            7: 0,  # sunday
            1: -1,  # monday
            2: -2,  # tuesday
            3: -3,  # wednesday
            4: -4,  # thursday
            5: -5,  # friday
            6: -6,  # saturday
        }
        return switcher.get(day)

    @classmethod
    def utc_to_local(cls, utc_dt, local_timezone):
        return (utc_dt.replace(tzinfo=datetime.timezone.utc).astimezone(tz=local_timezone)).replace(tzinfo=None)

    async def set_local_timezone(self):
        self.local_timezone = await async_get_time_zone(str(self._timezone))

    async def get_shabbat_time_in(self):
        """Get Shabbat entrance time"""
        if self.shabbat_in:
            return self.is_time_format(str(self.shabbat_in)[11:16])
        return LANGUAGE_DATA[self._language][0]

    async def get_shabbat_time_out(self):
        """Get Shabbat exit time"""
        if self.shabbat_out:
            return self.is_time_format(str(self.shabbat_out)[11:16])
        return LANGUAGE_DATA[self._language][0]

    async def get_yomtov_time_in(self):
        """Get Shabbat entrance time"""
        today = self.utc_to_local(datetime.datetime.utcnow(), self.local_timezone)
        if self.yomtov_in and self.yomtov_out:
            if self.yomtov_out.date() > today.date():
                return self.is_time_format(str(self.yomtov_in)[11:16])
        return LANGUAGE_DATA[self._language][0]

    async def get_yomtov_time_out(self):
        """Get Shabbat exit time"""
        today = self.utc_to_local(datetime.datetime.utcnow(), self.local_timezone)
        if self.yomtov_in and self.yomtov_out:
            if self.yomtov_out.date() > today.date():
                return self.is_time_format(str(self.yomtov_out)[11:16])
        return LANGUAGE_DATA[self._language][0]

    async def get_parasha(self) -> str:
        """Get parashat hashavo'h."""
        result = LANGUAGE_DATA[self._language][2]
        for extract_data in self.hebcal_db:
            if "shabbat" in list(extract_data.values()):
                return self.parashat + " , " + extract_data["title"]
        if self.parashat is None:
            for extract_data in self.hebcal_db:
                if "holiday" in list(extract_data.values()):
                    start = datetime.datetime.strptime(
                        extract_data["date"], "%Y-%m-%d"
                    )
                    if start.date() == self.shabbat_out.date():
                        self.parashat = "חג " + extract_data["title"]
        return self.parashat if self.parashat is not None else result

    async def get_event_name(self) -> str:
        """Get event name."""
        if self._language == "hebrew":
            result = HEBREW_WEEKDAY[datetime.datetime.today().isoweekday()]
        else:
            result = str(datetime.date.today().strftime("%A")) + ","
        today = self.utc_to_local(datetime.datetime.utcnow(), self.local_timezone)
        holiday = None
        roshchodesh = None
        try:
            for extract_data in self.hebcal_db:
                if "holiday" in list(extract_data.values()):
                    start = datetime.datetime.strptime(
                        extract_data["start"], "%Y-%m-%dT%H:%M:%S"
                    )
                    end = datetime.datetime.strptime(
                        extract_data["end"], "%Y-%m-%dT%H:%M:%S"
                    )
                    if start < today < end:
                        holiday = extract_data["title"]
                elif "roshchodesh" in list(extract_data.values()):
                    start = datetime.datetime.strptime(
                        extract_data["start"], "%Y-%m-%dT%H:%M:%S"
                    )
                    end = datetime.datetime.strptime(
                        extract_data["end"], "%Y-%m-%dT%H:%M:%S"
                    )
                    if start < today < end:
                        roshchodesh = extract_data["hebrew"]
            if holiday is not None:
                result = result + " " + holiday
            if roshchodesh is not None:
                result = result + " " + roshchodesh
            if not holiday and not roshchodesh:
                result = LANGUAGE_DATA[self._language][1]
        except Exception as e:
            _LOGGER.error(str(e))
        return result

    async def get_omer_day(self) -> str:
        """Get event name."""
        result = LANGUAGE_DATA[self._language][3]
        today = self.utc_to_local(datetime.datetime.utcnow(), self.local_timezone)
        try:
            for extract_data in self.hebcal_db:
                if "omer" in list(extract_data.values()):
                    start = datetime.datetime.strptime(
                        extract_data["start"], "%Y-%m-%dT%H:%M:%S"
                    )
                    end = datetime.datetime.strptime(
                        extract_data["end"], "%Y-%m-%dT%H:%M:%S"
                    )
                    if start < today < end:
                        omer = extract_data["hebrew"]
                        omer = re.findall(r'\d+', omer)
                        result = OMER_DAYS[self._omer_count_type][int(omer[0])]
                        self.omer = True
                    else:
                        self.omer = False
        except Exception as e:
            _LOGGER.error(str(e))
        return result

    async def is_shabbat(self) -> str:
        """Check if it is Shabbat now"""
        today = self.utc_to_local(datetime.datetime.utcnow(), self.local_timezone)
        if self.shabbat_in is not None and self.shabbat_out is not None:
            is_in = self.shabbat_in - datetime.timedelta(minutes=int(self._time_before))
            is_out = self.shabbat_out + datetime.timedelta(
                minutes=int(self._time_after)
            )
            if is_in < today < is_out:
                return "True"
            return "False"
        return LANGUAGE_DATA[self._language][0]

    async def is_yomtov(self) -> str:
        """Check if it is yomtov now"""
        today = self.utc_to_local(datetime.datetime.utcnow(), self.local_timezone)
        if self.yomtov_in is not None and self.yomtov_out is not None:
            is_in = self.yomtov_in - datetime.timedelta(minutes=int(self._time_before))
            is_out = self.yomtov_out + datetime.timedelta(
                minutes=int(self._time_after)
            )
            if is_in < today < is_out:
                return "True"
            return "False"
        return LANGUAGE_DATA[self._language][0]

    async def get_yomtov_name(self) -> str:
        """Get yomtov name"""
        result = LANGUAGE_DATA[self._language][0]
        try:
            for extract_data in self.hebcal_db:
                for x in extract_data.keys():
                    if x == "yomtov":
                        today = self.utc_to_local(datetime.datetime.utcnow(), self.local_timezone)
                        date = datetime.datetime.strptime(extract_data["date"][:10], "%Y-%m-%d").date()
                        if date > today.date():
                            result = HEBREW_WEEKDAY[date.isoweekday()]
                            result = result + " " + extract_data["title"]
                            return result
        except Exception as e:
            _LOGGER.error(str(e))
        return result

    async def get_hebrew_date(self) -> str:
        """Convert to hebrew date"""
        if self._language == "hebrew":
            day = HEBREW_WEEKDAY[datetime.datetime.today().isoweekday()]
            return day + self.hebcal_db[-1]["hebrew"]
        else:
            day = datetime.date.today().strftime("%A")
            return day + ", " + self.hebcal_db[-1]["english"]

    async def get_zmanim(self):
        return "זמנים הלכתיים עבור יום " + str(self.file_time_stamp)

    @classmethod
    def is_time_format(cls, input_time) -> str:
        """Check if the time is correct"""
        try:
            time.strptime(input_time, "%H:%M")
            return input_time
        except ValueError:
            return "Error"
