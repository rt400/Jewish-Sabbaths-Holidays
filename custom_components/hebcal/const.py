"""Constants"""
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_LATITUDE, CONF_LONGITUDE, CONF_RESOURCES

SENSOR_PREFIX = "Hebcal "
HAVDALAH_MINUTES = "havdalah_calc"
TIME_BEFORE_CHECK = "time_before_check"
TIME_AFTER_CHECK = "time_after_check"

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

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_LATITUDE): cv.latitude,
        vol.Optional(CONF_LONGITUDE): cv.longitude,
        vol.Optional(HAVDALAH_MINUTES, default=42): int,
        vol.Optional(TIME_BEFORE_CHECK, default=10): int,
        vol.Optional(TIME_AFTER_CHECK, default=10): int,
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
