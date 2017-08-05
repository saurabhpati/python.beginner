# you can also get the calendar for the month.
import calendar;

year = input('Give the year of the calendar required:');

try:
    year = int(year);
except:
    print('Please give only integers as input');
    exit();

month = input('Give the month of the calendar required:').lower();

monthDictionary = {
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'july': 7,
    'august': 8,
    'september': 9,
    'october': 10,
    'november': 11,
    'december': 12,
};

isMonthString = month in monthDictionary.keys();
isMonthInt = month in monthDictionary.values();

if not isMonthInt and not isMonthString:
    print('Invalid input');
    exit();

if isMonthInt:
    print(calendar.month(year, month));

if isMonthString:
    print(calendar.month(year, monthDictionary[month]));