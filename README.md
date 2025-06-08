[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)
# Jewish Sabbaths and Holidays Times integration for Home-Assistant

The `Jewish-Sabbaths-Holidays` platform uses the [HebCal API](https://www.hebcal.com/) to receive Shabbat times and the times of Jewish holidays, as well as the Hebrew date and the names of Jewish holidays (chagim).

## Installation

To install the integration, first download all the files in this folder: <https://github.com/rt400/Jewish-Sabbaths-Holidays/tree/master/custom_components/hebcal>.

Then create a folder called `hebcal` in your HomeAssistant `config/custom_components` folder and copy all files that you already download.

In order to display the correct times, the sensor needs your geolocation. By default it receives this from the instance's `configuration.yaml`.

You can configure your geolocation as follows:

```YAML
   homeassistant:
     latitude: 32.0667
     longitude: 34.7667
     time_zone: Asia/Jerusalem
```

If you don't know your geocoordinates, you can find them [here](https://www.latlong.net/). 

The sensor also requires [TimeZone](https://www.home-assistant.io/blog/2015/05/09/utc-time-zone-awareness/) to work.

To install using [HACS (Home Assistant Community Store)](https://hacs.xyz/), add this repository to your HACS custom repositories and select type -> integration.

When it shows up, click Install.

## Configuration

To enable `hebcal` times , just add the following lines to your `configuration.yaml`:

```yaml
# Example configuration.yaml entry
sensor:
  - platform: hebcal
    resources:
      - shabbat_in
      - shabbat_out
```

### Optional Configuration Variables

You can configure the time for havdala and the time for the entry of Shabbat by modifying the following parameters:

- **havdalah_calc**       # By default this is set to 42 minutes. You can also configure this value to be 50 minutes, 70 minutes, 72 minutes, or some other value.

- **time_before_check**   #  By default this is set to 10 minutes. You can modify the value in minutes.

- **time_after_check**    # By default this is set to 10 minutes. You can modify this value.

- **jerusalem_candle**    # By default this value is set to 'False'. To enable Jerusalem candle lighting time (40 minutes before Shabbat), change the value to 'True'. 

- **tzeit_hakochavim**    # By default this is set to 'True'. If it is set to false, the sensor uses the time set for havdala.

- **israel_diaspora**    # By default this is set to 'True'. If it is set to false, the sensor set time by diaspora and not by israel (עבור יהודי התפוצות שהחגים אצלהם כפולים)

- **omer_count_type**     # By default this is set to 0. 1 configures the omer counting method to follow the Yemenite/Teimani tradition. 2 is Ashkenazi and Sephardic.

- **language**            #  By default this is set to Hebrew. But you can choose to display values in one of the supported languages by specifying the language (the options are: English, Hebrew, German, Spanish, French, Russian, Polish, Finish, Russian, and Hungarian).

-  **use_12h_time**            #  By default this is set to False. But you can choose to display time values in 12H instead 24H.

- **resources:**          # Mandatory - You need to select at least one resource for the integration to work correctly.

```yaml
    - shabbat_in     # get shabbat entrace
    - shabbat_out    # get shabbat exit
    - parasha        # get parashat haShavoh
    - hebrew_date    # get the hebrew date on every day (changed in 00:00)
    - is_shabbat     # get if shabbat or not by True or False.
    - yomtov_in     # get yomtov entrace
    - yomtov_out    # get yomtov exit
    - is_yomtov     # get if yomtov or not by True or False.
    - yomtov_name    # get yomtov name.
    - event_name     # get event name.
    - omer_day       # get omer name.
    - zmanim       # get zmanim for the current day
```

## Full configuration example

The following sample configuration shows a configuration with all the resources loaded:

```yaml
# Example configuration.yaml entry
sensor:
  - platform: hebcal
    havdalah_calc: 42
    time_before_check: 10
    time_after_check: 1
    jerusalem_candle: false
    tzeit_hakochavim: false
    israel_diaspora: true
    use_12h_time: false
    omer_count_type: 0
    language: english
    resources:
      - shabbat_in
      - shabbat_out
      - parasha
      - hebrew_date
      - is_shabbat
      - yomtov_in
      - yomtov_out
      - is_yomtov
      - yomtov_name
      - event_name
      - omer_day
      - zmanim
```

  **Good Luck !**
