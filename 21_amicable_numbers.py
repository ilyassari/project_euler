'''
Problem 21 Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from aritmetic import all_factors

def d(n):
    """take a number; give sum of all factors"""
    return sum(all_factors(n))

def check_amicable_numbers(number):
    """ take a number, give its an amicable number or not """
    return number == d(d(number)) and number != d(number)

def amicable_numbers(boundary):
    """take a number as upper limit; give amicable numbers as list"""
    nums = list()
    for i in range(1, boundary):
        if check_amicable_numbers(i):
            nums.append(i)
    return nums

def sum_of_amicable_numbers(boundary):
    """take a number as upper limit; give sum of amicable numbers"""
    return sum(amicable_numbers(boundary))


print(sum_of_amicable_numbers(10000)) #31626
