[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)
# Jewish Sabbaths and Holidays Times integration for Home-Assistant

The `Jewish-Sabbaths-Holidays` platform uses [HebCal API](https://www.hebcal.com/) to Receive Shabbat and holiday entry times, as well as the Hebrew date and Jewish holiday names.

## Installation

First download all files in folder <https://github.com/rt400/Jewish-Sabbaths-Holidays/tree/master/custom_components/hebcal>.
Now you need to create folder "hebcal" in your HomeAssistant config/custom_components folder and copy all files that you already download.

The sensor need latitude and longitude and timezone so he got it from HomeAssitant config,
   so you need to besure that you put them in configuration.yaml.

   also need the TimeZone
   see link : <https://www.home-assistant.io/blog/2015/05/09/utc-time-zone-awareness/>
   Example :

   ```yaml
      homeassistant:
        latitude: 32.0667
        longitude: 34.7667
        time_zone: Asia/Jerusalem
   ```

-----

To install using [HACS (Home Assistant Community Store)](https://hacs.xyz/), add this repository to your HACS custom repositories and select type -> integration.
When it shows up, click Install.

## Configuration

To enable hebcal times , just add the following lines to your `configuration.yaml`:

```yaml
# Example configuration.yaml entry
sensor:
  - platform: hebcal
    resources:
      - shabbat_in
      - shabbat_out
```

### Optional Configuration Variables

If you want to control the time off Havdala and time before entrace :

- **havdalah_calc**       # By defaule he get 42 Min , you can set 50Min or 72Min for other methods

- **time_before_check**   # By defaule he get 10 Min , you can set minutes so the sensor can check if is shabbat

- **time_after_check**    # By defaule he get 10 Min , you can set minutes so the sensor can check if shabbat is ends..

- **jerualem_candle**    # By defaule he get False , If set True the candle light will be like in Jerualem time(40 Mins)

- **tzeit_hakochavim**    # By defaule set True , If set False the havdalah exit use calc

- **omer_count_type**     # By defaule set to 0 ( 0 - Yeman , 1 - Eshkenaz/Sfard ) , set the nosah omer count day

- **language**            # By defaule set to hebrew ( english, hebrew, german, spanish, french, russian, polish, finnish, hungarian) , set the language

- **resources:**          # Mandatory - You need to select atleast one

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
    - zmnaim         # get zmanim for the current day
```

## Full configuration example

The configuration sample below shows how an entry can look like:

```yaml
# Example configuration.yaml entry
sensor:
  - platform: hebcal
    havdalah_calc: 42
    time_before_check: 10
    time_after_check: 1
    jerualem_candle: False
    tzeit_hakochavim: False
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
