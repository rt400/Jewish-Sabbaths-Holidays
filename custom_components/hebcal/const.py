"""Constants"""
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_LATITUDE, CONF_LONGITUDE, CONF_RESOURCES

PLATFORM_FOLDER = "/custom_components/hebcal/"

HEBCAL_SHABBAT_URL_HAVDALAH = "https://www.hebcal.com/shabbat?cfg=json&geo=pos&leyning=off&a=off&gy={}&gm={}&gd={}" \
                              "&latitude={}&longitude={}&tzid={}&m={}"
HEBCAL_SHABBAT_URL = "https://www.hebcal.com/shabbat?cfg=json&geo=pos&leyning=off&a=off&gy={}&gm={}&gd={}" \
                     "&latitude={}&longitude={}&tzid={}"

HEBCAL_DATE_URL_HAVDALAH = "https://www.hebcal.com/hebcal/?v=1&cfg=json&maj=on&min=on&nx=on&mf=on&ss=on&mod=on" \
                           "&s=on&c=on&o=on&i=on&geo=pos&lg=h&start={}&end={}&latitude={}&longitude={}" \
                           "&tzid={}&m={}"
HEBCAL_DATE_URL = "https://www.hebcal.com/hebcal/?v=1&cfg=json&maj=on&min=on&nx=on&mf=on&ss=on&mod=on&s=on&c=on" \
                  "&o=on&i=on&geo=pos&lg=h&start={}&end={}&latitude={}&longitude={}&tzid={}"

HEBCAL_CONVERTER_URL = "https://www.hebcal.com/converter/?cfg=json&gy={}&gm={}&gd={}&g2h=1"

SENSOR_PREFIX = "Hebcal "
HAVDALAH_MINUTES = "havdalah_calc"
TIME_BEFORE_CHECK = "time_before_check"
TIME_AFTER_CHECK = "time_after_check"
TZEIT_HAKOCHAVIM = "tzeit_hakochavim"

SENSOR_TYPES = {
    "shabbat_in": ["כניסת השבת", "mdi:candle", "shabbat_in"],
    "shabbat_out": ["צאת השבת", "mdi:exit-to-app", "shabbat_out"],
    "is_shabbat": ["האם שבת", "mdi:candle", "is_shabbat"],
    "parasha": ["פרשת השבוע", "mdi:book-open-variant", "parasha"],
    "holiday_in": ["כניסת החג", "mdi:candle", "holiday_in"],
    "holiday_out": ["צאת החג", "mdi:exit-to-app", "holiday_out"],
    "is_holiday": ["האם חג", "mdi:candle", "is_holiday"],
    "holiday_name": ["שם החג", "mdi:book-open-variant", "holiday_name"],
    "hebrew_date": ["תאריך עברי", "mdi:calendar", "hebrew_date"],
}

HEBREW_WEEKDAY = {7: "יום ראשון, ",
                  1: "יום שני, ",
                  2: "יום שלישי, ",
                  3: "יום רביעי, ",
                  4: "יום חמישי, ",
                  5: "יום שישי, ",
                  6: "יום שבת, "}

FRIDAY_DAY = {7: 5,
              1: 4,
              2: 3,
              3: 2,
              4: 1,
              5: 0,
              6: -1, }
              
DEFAULT_HAVDALAH_MINUTES = 42
DEFAULT_TIME_BEFORE_CHECK = 10
DEFAULT_TIME_AFTER_CHECK = 10
DEFAULT_TZEIT_HAKOCHAVIM = True

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_LATITUDE): cv.latitude,
        vol.Optional(CONF_LONGITUDE): cv.longitude,
        vol.Optional(HAVDALAH_MINUTES, default=DEFAULT_HAVDALAH_MINUTES): cv.positive_int,
        vol.Optional(TIME_BEFORE_CHECK, default=DEFAULT_TIME_BEFORE_CHECK): cv.positive_int,
        vol.Optional(TIME_AFTER_CHECK, default=DEFAULT_TIME_AFTER_CHECK): cv.positive_int,
        vol.Optional(TZEIT_HAKOCHAVIM, default=DEFAULT_TZEIT_HAKOCHAVIM): cv.boolean,
        vol.Optional(
            CONF_RESOURCES,
            default=[
                "shabbat_in",
                "shabbat_out",
                "parasha",
                "hebrew_date",
                "is_shabbat",
                "holiday_in",
                "holiday_out",
                "is_holiday",
                "holiday_name",
            ],
        ): vol.All(cv.ensure_list, [vol.In(SENSOR_TYPES)]),
    }
)
