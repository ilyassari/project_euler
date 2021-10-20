"""
Problem 23 Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from math import ceil
from arithmetic import all_factors
import time

def check_abundant(number):
    """ take number return it was abundant or not """
    return sum(all_factors(number)) > number

def sum_two_abundant(number):
    """ take number return it could be written as the sum of two abundant numbers or not """
    for i in range(1, ceil((number / 2) + 1)):
        if check_abundant(i) and check_abundant(number - i):
            return True
    return False

def non_abundant_sum(boundary):
    """ take a upper limit return summ of all positive integers which cannot be written as the sum of two abundant numbers"""
    return sum(list(filter(lambda x: (sum_two_abundant(x) == False), range(1, boundary))))


begin_time = time.time()
print(non_abundant_sum(28123)) #4179871
end_time = time.time()
print(f"Elapsed time : {end_time - begin_time:0.4f} second") #Elapsed time : 5837.1397 second
