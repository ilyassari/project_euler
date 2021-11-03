'''
Problem 17 Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" , "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "onehundred"]

def make_letter(number):
    """take an integer and gives its spelling without spaces or hyphens"""
    if number <= 19:
        return ones[number]
    elif number <= 99:
        return tens[int(number / 10)] + ones[number % 10]
    elif number <= 999:
        if number % 100 == 0:
            return ones[int(number / 100)] + "hundred"
        else:
            return ones[int(number / 100)] + "hundred" + "and" + make_letter(number % 100)
    elif number <= 9999:
        if number % 1000 == 0:
            return ones[int(number / 1000)] + "thousand"
        else:
            return ones[int(number / 1000)] + "thousand" + "and" + make_letter(number % 1000)
    else:
        return "error"

def count_letter(begin, end):
    """take two integer and count letter between that numbers
    both number are included """
    counter = 0
    for i in range (begin, end + 1):
        counter += len(make_letter(i))
    return counter


print(count_letter(1,1000)) #21124
