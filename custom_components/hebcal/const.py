"""Constants"""

PLATFORM_FOLDER = "/custom_components/hebcal/"

HEBCAL_DATE_URL_HAVDALAH = "https://www.hebcal.com/hebcal/?v=1&cfg=json&maj=on&min=on&nx=on&mf=on&ss=on&mod=on" \
                           "&s=on&c=on&o=on&i=on&geo=pos&lg={}&start={}&end={}&latitude={}&longitude={}" \
                           "&tzid={}&m={}&b={}"

HEBCAL_DATE_URL = "https://www.hebcal.com/hebcal/?v=1&cfg=json&maj=on&min=on&nx=on&mf=on&ss=on&mod=on&s=on&c=on" \
                  "&o=on&i=on&geo=pos&lg={}&start={}&end={}&latitude={}&longitude={}&tzid={}&b={}"

HEBCAL_ZMANIM_URL = "https://www.hebcal.com/zmanim?cfg=json&geo=pos&latitude={}&longitude={}&tzid={}&date={}"

HEBCAL_CONVERTER_URL = "https://www.hebcal.com/converter/?cfg=json&gy={}&gm={}&gd={}&g2h=1"

SENSOR_PREFIX = "Hebcal "
HAVDALAH_MINUTES = "havdalah_calc"
TIME_BEFORE_CHECK = "time_before_check"
TIME_AFTER_CHECK = "time_after_check"
JERUSALEM_CANDLE = "jerusalem_candle"
TZEIT_HAKOCHAVIM = "tzeit_hakochavim"
OMER_COUNT_TYPE = "omer_count_type"
LANGUAGE = "language"
USE_12H_TIME = "use_12h_time"

DEFAULT_HAVDALAH_MINUTES = 42
DEFAULT_TIME_BEFORE_CHECK = 10
DEFAULT_TIME_AFTER_CHECK = 10
DEFAULT_JERUSALEM_CANDLE = False
DEFAULT_TZEIT_HAKOCHAVIM = True
DEFAULT_OMER_COUNT_TYPE = 0
DEFAULT_USE_12H_TIME = False
DEFAULT_LANGUAGE = "hebrew"

LANGUAGE_DATA = {
    "english": ["No Info", "No Event", "Special Shabbat", "No Omer Count",
                {'chatzotNight': 'Midnight', 'alotHaShachar': 'Alot Ha Shachar',
                 'misheyakir': ' Time for Talit and Tefilin',
                 'misheyakirMachmir': 'Time for Talit and Tefilin - Strictness',
                 'dawn': 'Dawn', 'sunrise': 'Sunrize', 'sofZmanShma': 'End Time Of Shma',
                 'sofZmanTfilla': 'End Time Of Shaarit', 'chatzot': 'Midday', 'minchaGedola': 'Mincha Gedola',
                 'minchaKetana': 'Mincha Ketana', 'plagHaMincha': 'Plag HaMincha', 'sunset': 'Sunset',
                 'dusk': 'Dusk', }, "s"],
    "hebrew": ["אין מידע", "אין אירוע", "שבת מיוחדת", "אין ספירת העומר",
               {'chatzotNight': 'חצות לילה', 'alotHaShachar': 'עלות השחר', 'misheyakir': 'זמן הנחת טלית ותפילין',
                'misheyakirMachmir': 'זמן הנחת טלית ותפילין - מחמיר', 'dawn': 'שחר', 'sunrise': 'זריחה',
                'sofZmanShma': 'סוף זמן קריאת שמע', 'sofZmanTfilla': 'סוף זמן תפילת שחרית', 'chatzot': 'חצות היום',
                'minchaGedola': 'מנחה גדולה', 'minchaKetana': 'מנחה קטנה', 'plagHaMincha': 'פלג המנחה',
                'sunset': 'שקיעה', 'dusk': 'בין הערבים'}, "h"],
    "german": ["Keine Info", "Kein Ereignis", "Besonderer Schabbat", "Keine Omerzählung",
               {'chatzotNight': 'Midnight', 'alotHaShachar': 'Alot Ha Shachar',
                'misheyakir': ' Time for Talit and Tefilin',
                'misheyakirMachmir': 'Time for Talit and Tefilin - Strictness',
                'dawn': 'Dawn', 'sunrise': 'Sunrize', 'sofZmanShma': 'End Time Of Shma',
                'sofZmanTfilla': 'End Time Of Shaarit', 'chatzot': 'Midday', 'minchaGedola': 'Mincha Gedola',
                'minchaKetana': 'Mincha Ketana', 'plagHaMincha': 'Plag HaMincha', 'sunset': 'Sunset',
                'dusk': 'Dusk', }, "de"],
    "spanish": ["Sin información", "Sin evento", "Shabat especial", "Sin recuento de Omer",
                {'chatzotNight': 'Midnight', 'alotHaShachar': 'Alot Ha Shachar',
                 'misheyakir': ' Time for Talit and Tefilin',
                 'misheyakirMachmir': 'Time for Talit and Tefilin - Strictness',
                 'dawn': 'Dawn', 'sunrise': 'Sunrize', 'sofZmanShma': 'End Time Of Shma',
                 'sofZmanTfilla': 'End Time Of Shaarit', 'chatzot': 'Midday', 'minchaGedola': 'Mincha Gedola',
                 'minchaKetana': 'Mincha Ketana', 'plagHaMincha': 'Plag HaMincha', 'sunset': 'Sunset',
                 'dusk': 'Dusk', }, "es"],
    "french": ["Pas d'infos", "Pas d'événement", "Chabbat spécial", "Pas de décompte d'Omer",
               {'chatzotNight': 'Midnight', 'alotHaShachar': 'Alot Ha Shachar',
                'misheyakir': ' Time for Talit and Tefilin',
                'misheyakirMachmir': 'Time for Talit and Tefilin - Strictness',
                'dawn': 'Dawn', 'sunrise': 'Sunrize', 'sofZmanShma': 'End Time Of Shma',
                'sofZmanTfilla': 'End Time Of Shaarit', 'chatzot': 'Midday', 'minchaGedola': 'Mincha Gedola',
                'minchaKetana': 'Mincha Ketana', 'plagHaMincha': 'Plag HaMincha', 'sunset': 'Sunset',
                'dusk': 'Dusk', }, "fr"],
    "russian": ["Нет информации", "Нет событий", "Особый Шаббат", "Нет счета Омера",
                {'chatzotNight': 'Midnight', 'alotHaShachar': 'Alot Ha Shachar',
                 'misheyakir': ' Time for Talit and Tefilin',
                 'misheyakirMachmir': 'Time for Talit and Tefilin - Strictness',
                 'dawn': 'Dawn', 'sunrise': 'Sunrize', 'sofZmanShma': 'End Time Of Shma',
                 'sofZmanTfilla': 'End Time Of Shaarit', 'chatzot': 'Midday', 'minchaGedola': 'Mincha Gedola',
                 'minchaKetana': 'Mincha Ketana', 'plagHaMincha': 'Plag HaMincha', 'sunset': 'Sunset',
                 'dusk': 'Dusk', }, "ru"],
    "polish": ["Brak informacji", "Brak wydarzenia", "Specjalny szabat", "Bez liczenia omerów",
               {'chatzotNight': 'Midnight', 'alotHaShachar': 'Alot Ha Shachar',
                'misheyakir': ' Time for Talit and Tefilin',
                'misheyakirMachmir': 'Time for Talit and Tefilin - Strictness',
                'dawn': 'Dawn', 'sunrise': 'Sunrize', 'sofZmanShma': 'End Time Of Shma',
                'sofZmanTfilla': 'End Time Of Shaarit', 'chatzot': 'Midday', 'minchaGedola': 'Mincha Gedola',
                'minchaKetana': 'Mincha Ketana', 'plagHaMincha': 'Plag HaMincha', 'sunset': 'Sunset',
                'dusk': 'Dusk', }, "pl"],
    "finnish": ["Ei tietoja", "Ei tapahtumia", "Erityinen sapatti", "Ei Omer Count",
                {'chatzotNight': 'Midnight', 'alotHaShachar': 'Alot Ha Shachar',
                 'misheyakir': ' Time for Talit and Tefilin',
                 'misheyakirMachmir': 'Time for Talit and Tefilin - Strictness',
                 'dawn': 'Dawn', 'sunrise': 'Sunrize', 'sofZmanShma': 'End Time Of Shma',
                 'sofZmanTfilla': 'End Time Of Shaarit', 'chatzot': 'Midday', 'minchaGedola': 'Mincha Gedola',
                 'minchaKetana': 'Mincha Ketana', 'plagHaMincha': 'Plag HaMincha', 'sunset': 'Sunset',
                 'dusk': 'Dusk', }, "fi"],
    "hungarian": ["Nincs információ", "Nincs esemény", "Különleges szombat", "Nincs Omer gróf",
                  {'chatzotNight': 'Midnight', 'alotHaShachar': 'Alot Ha Shachar',
                   'misheyakir': ' Time for Talit and Tefilin',
                   'misheyakirMachmir': 'Time for Talit and Tefilin - Strictness',
                   'dawn': 'Dawn', 'sunrise': 'Sunrize', 'sofZmanShma': 'End Time Of Shma',
                   'sofZmanTfilla': 'End Time Of Shaarit', 'chatzot': 'Midday', 'minchaGedola': 'Mincha Gedola',
                   'minchaKetana': 'Mincha Ketana', 'plagHaMincha': 'Plag HaMincha', 'sunset': 'Sunset',
                   'dusk': 'Dusk', }, "hu"],
}

SENSOR_TYPES = {
    "shabbat_in": ["כניסת השבת", "mdi:candle", "Shabbat entry"],
    "shabbat_out": ["צאת השבת", "mdi:exit-to-app", "Shabbat came out"],
    "is_shabbat": ["האם שבת", "mdi:candle", "Is Shabbat?"],
    "parasha": ["פרשת השבוע", "mdi:book-open-variant", "Parasha"],
    "yomtov_in": ["כניסת יום טוב", "mdi:candle", "Yomtov entry"],
    "yomtov_out": ["צאת יום טוב", "mdi:exit-to-app", "Yomtov came out"],
    "is_yomtov": ["האם יום טוב", "mdi:candle", "Is Yomtov?"],
    "yomtov_name": ["יום טוב", "mdi:book-open-variant", "Yomtov Name"],
    "event_name": ["אירוע", "mdi:book-open-variant", "Event Name"],
    "omer_day": ["ספירת העומר", "mdi:book-open-variant", "Omer Count Day"],
    "hebrew_date": ["תאריך עברי", "mdi:calendar", "Hebrew Date"],
    "zmanim": ["זמנים הלכתיים", "mdi:calendar", "Zmanim"],
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

OMER_DAYS = [
    {
        1: "הַאידַּנָא חַד יוֹמָא בְּעֻמרָא",
        2: "הַאידַּנָא תְּרֵין יוֹמֵי בְּעֻמרָא",
        3: "הַאידַּנָא תְּלָתָא יוֹמֵי בְּעֻמרָא",
        4: "הַאידַּנָא אַרבְּעָא יוֹמֵי בְּעֻמרָא",
        5: "הַאידַּנָא חַמשָׁא יוֹמֵי בְּעֻמרָא",
        6: "הַאידַּנָא שִׁתָּא יוֹמֵי בְּעֻמרָא",
        7: "הַאידַּנָא שִׁבעָא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן חַד שָׁבוּעָא",
        8: "הַאידַּנָא תְּמָניָא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן חַד שָׁבוּעָא וְחַד יוֹמָא",
        9: "הַאידַּנָא תִּשׁעָא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן חַד שָׁבוּעָא וּתרֵין יוֹמֵי",
        10: "הַאידַּנָא עַשׂרָא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן חַד שָׁבוּעָא וּתלָתָא יוֹמֵי",
        11: "הַאידַּנָא חַד עֲשַׂר יוֹמֵי בְּעֻמרָא, דְּאִנּוּן חַד שָׁבוּעָא וְאַרבְּעָא יוֹמֵי",
        12: "הַאידַּנָא תְּרֵי עֲשַׂר יוֹמֵי בְּעֻמרָא, דְּאִנּוּן חַד שָׁבוּעָא וְחַמשָׁא יוֹמֵי",
        13: "הַאידַּנָא תְּלָת עֲשַׂר יוֹמֵי בְּעֻמרָא, דְּאִנּוּן חַד שָׁבוּעָא וְשִׁתָּא יוֹמֵי",
        14: "הַאידַּנָא אַרבַּעַת עֲשַׂר יוֹמֵי בְּעֻמרָא, דְּאִנּוּן תְּרֵין שָׁבוּעֵי",
        15: "הַאידַּנָא חַמשַׁת עֲשַׂר יוֹמֵי בְּעֻמרָא, דְּאִנּוּן תְּרֵין שָׁבוּעֵי וְחַד יוֹמָא",
        16: "הַאידַּנָא שִׁתַּת עֲשַׂר יוֹמֵי בְּעֻמרָא, דְאִינּוּן תְּרֵין שָׁבוּעֵי וּתרֵין יוֹמֵי",
        17: "הַאידַּנָא שִׁבעַת עֲשַׂר יוֹמֵי בְּעֻמרָא, דְּאִנּוּן תְּרֵין שָׁבוּעֵי וּתלָתָא יוֹמֵי",
        18: "הַאידַּנָא תַּמנַת עֲשַׂר יוֹמֵי בְּעֻמרָא, דְּאִנּוּן תְּרֵין שָׁבוּעֵי וְאַרבְּעָא יוֹמֵי",
        19: "הַאידַּנָא תִּשׁעַת עֲשַׂר יוֹמֵי בְּעֻמרָא, דְּאִנּוּן תְּרֵין שָׁבוּעֵי וְחַמשָׁא יוֹמֵי",
        20: "הַאידַּנָא עַשׂרִין יוֹמֵי בְּעֻמרָא, דְּאִנּוּן תְּרֵין שָׁבוּעֵי וְשִׁתָּא יוֹמֵי",
        21: "הַאידַּנָא עַשׂרִין וְחַד יוֹמֵי בְּעֻמרָא, דְּאִנּוּן תְּלָתָא שָׁבוּעֵי",
        22: "הַאידַּנָא עַשׂרִין וּתרֵין יוֹמֵי בְּעֻמרָא, דְּאִנּוּן תְּלָתָא שָׁבוּעֵי וְחַד יוֹמָא",
        23: "הַאידַּנָא עַשׂרִין וּתלָתָא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן תְּלָתָא שָׁבוּעֵי וּתרֵין יוֹמֵי",
        24: "הַאידַּנָא עַשׂרִין וְאַרבְּעָא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן תְּלָתָא שָׁבוּעֵי וּתלָתָא יוֹמֵי",
        25: "הַאידַּנָא עַשׂרִין וְחַמשָׁא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן תְּלָתָא שָׁבוּעֵי וְאַרבְּעָא יוֹמֵי",
        26: "הַאידַּנָא עַשׂרִין וְשִׁתָּא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן תְּלָתָא שָׁבוּעֵי וְחַמשָׁא יוֹמֵי",
        27: "הַאידַּנָא עַשׂרִין וְשִׁבעָא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן תְּלָתָא שָׁבוּעֵי וְשִׁתָּא יוֹמֵי",
        28: "הַאידַּנָא עַשׂרִין וּתמָניָא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן אַרבְּעָא שָׁבוּעֵי",
        29: "הַאידַּנָא עַשׂרִין וְתִשׁעָא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן אַרבְּעָא שָׁבוּעֵי וְחַד יוֹמָא",
        30: "הַאידַּנָא תְּלָתִין יוֹמֵי בְּעֻמרָא, דְּאִנּוּן אַרבְּעָא שָׁבוּעֵי וּתרֵין יוֹמֵי",
        31: "הַאידַּנָא תְּלָתִין וְחַד יוֹמֵי בְּעֻמרָא, דְּאִנּוּן אַרבְּעָא שָׁבוּעֵי וּתלָתָא יוֹמֵי",
        32: "הַאידַּנָא תְּלָתִין וּתרֵין יוֹמֵי בְּעֻמרָא, דְּאִנּוּן אַרבְּעָא שָׁבוּעֵי וְאַרבְּעָא יוֹמֵי",
        33: "הַאידַּנָא תְּלָתִין וּתלָתָא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן אַרבְּעָא שָׁבוּעֵי וְחַמשָׁא יוֹמֵי",
        34: "הַאידַּנָא תְּלָתִין וְאַרבְּעָא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן אַרבְּעָא שָׁבוּעֵי וְשִׁתָּא יוֹמֵי",
        35: "הַאידַּנָא תְּלָתִין וְחַמשָׁא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן חַמשָׁא שָׁבוּעֵי",
        36: "הַאידַּנָא תְּלָתִין וְשִׁתָּא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן חַמשָׁא שָׁבוּעֵי וְחַד יוֹמָא",
        37: "הַאידַּנָא תְּלָתִין וְשִׁבעָא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן חַמשָׁא שָׁבוּעֵי וּתרֵין יוֹמֵי",
        38: "הַאידַּנָא תְּלָתִין וּתמָניָא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן חַמשָׁא שָׁבוּעֵי וּתלָתָא יוֹמֵי",
        39: "הַאידַּנָא תְּלָתִין וְתִשׁעָא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן חַמשָׁא שָׁבוּעֵי וְאַרבְּעָא יוֹמֵי",
        40: "הַאידַּנָא אַרבְּעִין יוֹמֵי בְּעֻמרָא, דְּאִנּוּן חַמשָׁא שָׁבוּעֵי וְחַמשָׁא יוֹמֵי",
        41: "הַאידַּנָא אַרבְּעִין וְחַד יוֹמֵי בְּעֻמרָא, דְּאִנּוּן חַמשָׁא שָׁבוּעֵי וְשִׁתָּא יוֹמֵי",
        42: "הַאידַּנָא אַרבְּעִין וּתרֵין יוֹמֵי בְּעֻמרָא, דְּאִנּוּן שִׁתָּא שָׁבוּעֵי",
        43: "הַאידַּנָא אַרבְּעִין וּתלָתָא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן שִׁתָּא שָׁבוּעֵי וְחַד יוֹמָא",
        44: "הַאידַּנָא אַרבְּעִין וְאַרבְּעָא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן שִׁתָּא שָׁבוּעֵי וּתרֵין יוֹמֵי",
        45: "הַאידַּנָא אַרבְּעִין וְחַמשָׁא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן שִׁתָּא שָׁבוּעֵי וּתלָתָא יוֹמֵי",
        46: "הַאידַּנָא אַרבְּעִין וְשִׁתָּא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן שִׁתָּא שָׁבוּעֵי וְאַרבְּעָא יוֹמֵי",
        47: "הַאידַּנָא אַרבְּעִין וְשִׁבעָא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן שִׁתָּא שָׁבוּעֵי וְחַמשָׁא יוֹמֵי",
        48: "הַאידַּנָא אַרבְּעִין וּתמָניָא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן שִׁתָּא שָׁבוּעֵי וְשִׁתָּא יוֹמֵי",
        49: "הַאידַּנָא אַרבְּעִין וְתִשׁעָא יוֹמֵי בְּעֻמרָא, דְּאִנּוּן שִׁבעָא שָׁבוּעֵי שַׁלמֵי"
    },
    {
        1: "הַיּוֹם יוֹם אֶחָד לָעֽוֹמֶר",
        2: "הַיוֹם שְׁנֵי יָמִים לָעֽוֹמֶר",
        3: "הַיוֹם שְׁלֹשָׁה יָמִים לָעֽוֹמֶר",
        4: "הַיוֹם אַרְבָּעָה יָמִים לָעֽוֹמֶר",
        5: "הַיוֹם חֲמִשָּׁה יָמִים לָעֽוֹמֶר",
        6: "הַיוֹם שִׁשָׁה יָמִים לָעֽוֹמֶר",
        7: "הַיוֹם שִׁבְעָה יָמִים שֶׁהֵם שָׁבֽוּעַ אֶחָד לָעֽוֹמֶר",
        8: "הַיוֹם שְׁמוֹנָה יָמִים שֶׁהֵם שָׁבֽוּעַ אֶחָד וְיוֹם אֶחָד לָעֽוֹמֶר",
        9: "הַיוֹם תִּשְׁעָה יָמִים שֶׁהֵם שָׁבֽוּעַ אֶחָד וּשְׁנֵי יָמִים לָעֽוֹמֶר",
        10: "הַיוֹם עֲשָׂרָה יָמִים שֶׁהֵם שָׁבֽוּעַ אֶחָד וּשְׁלֹשָׁה יָמִים לָעֽוֹמֶר",
        11: "הַיוֹם אַחַד עָשָׂר יוֹם שֶׁהֵם שָׁבֽוּעַ אֶחָד וְאַרְבָּעָה יָמִים לָעֽוֹמֶר",
        12: "הַיוֹם שְׁנֵים עָשָׂר יוֹם שֶׁהֵם שָׁבֽוּעַ אֶחָד וַחֲמִשָׁה יָמִים לָעֽוֹמֶר",
        13: "הַיוֹם שְׁלֹשָׁה עָשָׂר יוֹם שֶׁהֵם שָׁבֽוּעַ אֶחָד וְשִׁשָׁה יָמִים לָעֽוֹמֶר",
        14: "הַיוֹם אַרְבָּעָה עָשָׂר יוֹם שֶׁהֵם שְׁנֵי שָׁבוּעוֹת לָעֽוֹמֶר",
        15: "הַיוֹם חֲמִשָׁה עָשָׂר יוֹם שֶׁהֵם שְׁנֵי שָׁבוּעוֹת וְיוֹם אֶחָד לָעֽוֹמֶר",
        16: "הַיוֹם שִׁשָׁה עָשָׂר יוֹם שֶׁהֵם שְׁנֵי שָׁבוּעוֹת וּשְׁנֵי יָמִים לָעֽוֹמֶר",
        17: "הַיוֹם שִׁבְעָה עָשָׂר יוֹם שֶׁהֵם שְׁנֵי שָׁבוּעוֹת וּשְׁלֹשָׁה יָמִים לָעֽוֹמֶר",
        18: "הַיוֹם שְׁמוֹנָה עָשָׂר יוֹם שֶׁהֵם שְׁנֵי שָׁבוּעוֹת וְאַרְבָּעָה יָמִים לָעֽוֹמֶר",
        19: "הַיוֹם תִּשְׁעָה עָשָׂר יוֹם שֶׁהֵם שְׁנֵי שָׁבוּעוֹת וַחֲמִשָׁה יָמִים לָעֽוֹמֶר",
        20: "הַיוֹם עֶשְׂרִים יוֹם שֶׁהֵם שְׁנֵי שָׁבוּעוֹת וְשִׁשָׁה יָמִים לָעֽוֹמֶר",
        21: "הַיוֹם אֶחָד וְעֶשְׂרִים יוֹם שֶׁהֵם שְׁלֹשָׁה שָׁבוּעוֹת לָעֽוֹמֶר",
        22: "הַיוֹם שְׁנַֽיִם וְעֶשְׂרִים יוֹם שֶׁהֵם שְׁלֹשָׁה שָׁבוּעוֹת וְיוֹם אֶחָד לָעֽוֹמֶר",
        23: "הַיוֹם שְׁלֹשָׁה וְעֶשְׂרִים יוֹם שֶׁהֵם שְׁלֹשָׁה שָׁבוּעוֹת וּשְׁנֵי יָמִים לָעֽוֹמֶר",
        24: "הַיוֹם אַרְבָּעָה וְעֶשְׂרִים יוֹם שֶׁהֵם שְׁלֹשָׁה שָׁבוּעוֹת וּשְׁלֹשָׁה יָמִים לָעֽוֹמֶר",
        25: "הַיוֹם חֲמִשָׁה וְעֶשְׂרִים יוֹם שֶׁהֵם שְׁלֹשָׁה שָׁבוּעוֹת וְאַרְבָּעָה יָמִים לָעֽוֹמֶר",
        26: "הַיוֹם שִׁשָׁה וְעֶשְׂרִים יוֹם שֶׁהֵם שְׁלֹשָׁה שָׁבוּעוֹת וַחֲמִשָׁה יָמִים לָעֽוֹמֶר",
        27: "הַיוֹם שִׁבְעָה וְעֶשְׂרִים יוֹם שֶׁהֵם שְׁלֹשָׁה שָׁבוּעוֹת וְשִׁשָׁה יָמִים לָעֽוֹמֶר",
        28: "הַיוֹם שְׁמוֹנָה וְעֶשְׂרִים יוֹם שֶׁהֵם אַרְבָּעָה שָׁבוּעוֹת לָעֽוֹמֶר",
        29: "הַיוֹם תִּשְׁעָה וְעֶשְׂרִים יוֹם שֶׁהֵם אַרְבָּעָה שָׁבוּעוֹת וְיוֹם אֶחָד לָעֽוֹמֶר",
        30: "הַיוֹם שְׁלֹשִׁים יוֹם שֶׁהֵם אַרְבָּעָה שָׁבוּעוֹת וּשְׁנֵי יָמִים לָעֽוֹמֶר",
        31: "הַיוֹם אֶחָד וּשְׁלֹשִׁים יוֹם שֶׁהֵם אַרְבָּעָה שָׁבוּעוֹת וּשְׁלֹשָׁה יָמִים לָעֽוֹמֶר",
        32: "הַיוֹם שְׁנַֽיִם וּשְׁלֹשִׁים יוֹם שֶׁהֵם אַרְבָּעָה שָׁבוּעוֹת וְאַרְבָּעָה יָמִים לָעֽוֹמֶר",
        33: "הַיוֹם שְׁלֹשָׁה וּשְׁלֹשִׁים יוֹם שֶׁהֵם אַרְבָּעָה שָׁבוּעוֹת וַחֲמִשָׁה יָמִים לָעֽוֹמֶר",
        34: "הַיוֹם אַרְבָּעָה וּשְׁלֹשִׁים יוֹם שֶׁהֵם אַרְבָּעָה שָׁבוּעוֹת וְשִׁשָׁה יָמִים לָעֽוֹמֶר",
        35: "הַיוֹם חֲמִשָׁה וּשְׁלֹשִׁים יוֹם שֶׁהֵם חֲמִשָׁה שָׁבוּעוֹת לָעֽוֹמֶר",
        36: "הַיוֹם שִׁשָׁה וּשְׁלֹשִׁים יוֹם שֶׁהֵם חֲמִשָׁה שָׁבוּעוֹת וְיוֹם אֶחָד לָעֽוֹמֶר",
        37: "הַיוֹם שִׁבְעָה וּשְׁלֹשִׁים יוֹם שֶׁהֵם חֲמִשָׁה שָׁבוּעוֹת וּשְׁנֵי יָמִים לָעֽוֹמֶר",
        38: "הַיוֹם שְׁמוֹנָה וּשְׁלֹשִׁים יוֹם שֶׁהֵם חֲמִשָׁה שָׁבוּעוֹת וּשְׁלֹשָׁה יָמִים לָעֽוֹמֶר",
        39: "הַיוֹם תִּשְׁעָה וּשְׁלֹשִׁים יוֹם שֶׁהֵם חֲמִשָׁה שָׁבוּעוֹת וְאַרְבָּעָה יָמִים לָעֽוֹמֶר",
        40: "הַיוֹם אַרְבָּעִים יוֹם שֶׁהֵם חֲמִשָׁה שָׁבוּעוֹת וַחֲמִשָׁה יָמִים לָעֽוֹמֶר",
        41: "הַיוֹם אֶחָד וְאַרְבָּעִים יוֹם שֶׁהֵם חֲמִשָׁה שָׁבוּעוֹת וְשִׁשָׁה יָמִים לָעֽוֹמֶר",
        42: "הַיוֹם שְׁנַֽיִם וְאַרְבָּעִים יוֹם שֶׁהֵם שִׁשָׁה שָׁבוּעוֹת לָעֽוֹמֶר",
        43: "הַיוֹם שְׁלֹשָׁה וְאַרְבָּעִים יוֹם שֶׁהֵם שִׁשָׁה שָׁבוּעוֹת וְיוֹם אֶחָד לָעֽוֹמֶר",
        44: "הַיוֹם אַרְבָּעָה וְאַרְבָּעִים יוֹם שֶׁהֵם שִׁשָׁה שָׁבוּעוֹת וּשְׁנֵי יָמִים לָעֽוֹמֶר",
        45: "הַיוֹם חֲמִשָׁה וְאַרְבָּעִים יוֹם שֶׁהֵם שִׁשָׁה שָׁבוּעוֹת וּשְׁלֹשָׁה יָמִים לָעֽוֹמֶר",
        46: "הַיוֹם שִׁשָׁה וְאַרְבָּעִים יוֹם שֶׁהֵם שִׁשָׁה שָׁבוּעוֹת וְאַרְבָּעָה יָמִים לָעֽוֹמֶר",
        47: "הַיוֹם שִׁבְעָה וְאַרְבָּעִים יוֹם שֶׁהֵם שִׁשָׁה שָׁבוּעוֹת וַחֲמִשָׁה יָמִים לָעֽוֹמֶר",
        48: "הַיוֹם שְׁמוֹנָה וְאַרְבָּעִים יוֹם שֶׁהֵם שִׁשָׁה שָׁבוּעוֹת וְשִׁשָׁה יָמִים לָעֽוֹמֶר",
        49: "הַיוֹם תִּשְׁעָה וְאַרְבָּעִים יוֹם שֶׁהֵם שִׁבְעָה שָׁבוּעוֹת לָעֽוֹמֶר"
    }
]
