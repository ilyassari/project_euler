"""
Problem 35 Circular primes

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

"""

from arithmetic import prime_list, prime_or_not
from stopwatch import stopwatch

def is_circular(number, checklist):
    "Take number and number list; return if its circular prime or not"
    checklist.sort()
    string_n = str(number)
    if len(string_n) == 1:
        return True
    temp = string_n
    for _ in range(1, len(string_n)):
        temp = temp[1:] + temp[0]
        if not int(temp) in checklist:
            if int(temp) < checklist[-1]:
                return False
            elif not prime_or_not(int(temp)):
                return False
    return True


@stopwatch
def circular_counter(checklist):
    "Take number list; return circular primes count in list"
    counter = 0
    for number in checklist:
        if is_circular(number, checklist):
            counter += 1
    return counter


print(circular_counter(prime_list(10 ** 6)))  # 55
