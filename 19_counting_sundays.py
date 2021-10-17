"""
Problem 19 Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import sys
sys.setrecursionlimit(1500)

def leap_year(year):
    """take year and give its leap year or not"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True #1600, 2000
            else:
                return False #1800, 1900
        else:
            return True #1904, 2016, 2020
    else:
        return False #1617, 2001, 2010

def day_index(day_name):
    """ take day name and give its order in week """
    days = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
    return days.index(day_name.lower())

def month_index(month_name):
    """ take month name and give its order in year """
    months = ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december")
    return months.index(month_name.lower())

def begin_day(year, month):
    """ take day year and month; give first day's index  """
    if leap_year(year):
        month_length = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    else:
        month_length = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if year == 1900 and month == 0:
        return 1
    else:
        if month == 0:
            previous = (year - 1 , 11)
        else:
            previous = (year, month - 1)
        return (begin_day(previous[0], previous[1]) + (month_length[previous[1]] % 7)) % 7


def check_first_day(year, month, day): #1919, 0, 2
    """ take day year, month and a day index; give if months' first day is same with the taken day """
    if begin_day(year, month) == day:
        return True
    return False

def count_first_day_in_period(begin_year, begin_month, end_year, end_month, day_name):
    """
    take a begin year as integer (must not lower than 1900) and month name as string
    take an end year as integer (must not lower than begin year) and month name as string
    take a name of day
    returns how many first days of the month fall on the specified day in the specified range
    """
    day_counter = 0
    for month in range (month_index(begin_month), 12):
        if check_first_day(begin_year, month, day_index(day_name)):
            day_counter += 1
    for year in range (begin_year + 1, end_year):
        for month in range(0,12):
            if check_first_day(year, month, day_index(day_name)):
                day_counter += 1
    for month in range (0, month_index(end_month) + 1):
        if check_first_day(end_year, month, day_index(day_name)):
            day_counter += 1
    return f"Number of days from {begin_year}:{begin_month} to {end_year}:{end_month} when the first day of the month is {day_name.lower()}: {day_counter}"



print(count_first_day_in_period(1901, "January", 2000, "December", "Sunday")) #171
