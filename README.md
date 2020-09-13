# Jewish Sabbaths and Holidays Times component for HomeAssistant

The `Jewish-Sabbaths-Holidays` platform uses to Receive Shabbat and holiday entry times, as well as a Hebrew date and Jewish holiday names.
This is base on Hebcal website.

***Note: If a holiday eve falls on a Saturday night then a holiday sensor will not work but a Shabbat sensor will be extended until Sunday evening (a holiday night that falls on a Sunday)***

## Installation

First download all files in folder https://github.com/rt400/Jewish-Sabbaths-Holidays/tree/master/custom_components/hebcal .
Now you need to create folder "hebcal" in your HomeAssistant config/custom_components folder and copy all files that you already download.

The sensor need latitude and longitude and timezone so he got it from HomeAssitant config ,
   so you need to besure that you put them in configuration.yaml . 
   
   also need the TimeZone 
   see link : https://www.home-assistant.io/blog/2015/05/09/utc-time-zone-awareness/
   Example :
   ```python
      homeassistant:
        latitude: 32.0667
        longitude: 34.7667
        time_zone: Asia/Jerusalem
   ```

## Configuration

To enable hebcal times , just add the following lines to your `configuration.yaml`:

```yaml
# Example configuration.yaml entry
sensor:
  - platform: hebcal
```

### Configuration Optinal Variables

If you want to control the time off Havdala and time before entrace :

**havdalah_calc** :   By defaule he get 42 Min , you can set 50Min or 72Min for other methods
  
**time_before_check** :  By defaule he get 10 Min , you can set minutes so the sensor can check if is shabbat
  
**time_after_check** : By defaule he get 10 Min , you can set minutes so the sensor can check if shabbat is ends..

**resources:**  (if not set you will get all.)
```
    - shabbat_in : get shabbat entrace
    - shabbat_out : get shabbat exit
    - parasha : get parashat haShavoh
    - hebrew_date : get the hebrew date on every day (changed in 00:00)
    - is_shabbat : get if shabbat or not by True or False.
    - holiday_in : get holiday entrace
    - holiday_out : get shabbat exit
    - is_holiday : get if holiday or not by True or False.
    - holiday_name : get Holiday name
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
    resources:
      - shabbat_in
      - shabbat_out
      - parasha
      - hebrew_date
      - is_shabbat
      - holiday_in
      - holiday_out
      - is_holiday
      - holiday_name
```
  
  **Good Luck !**
