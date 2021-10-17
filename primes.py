import math
from stopwatch import stopwatch

def prime_factorization(number):
    """ take a number and gives its all prime factors as a list"""
    divider = 2
    prime_factors = list()
    while divider <= number:
        while number % divider == 0:
            number = number / divider
            prime_factors.append(divider)
        divider += 1
    return prime_factors

def prime_or_not(number):
    """take a number and give its prime or not as boolean"""
    if number == 1:
        return False
    divider = 2
    square = math.sqrt(number)
    while divider <= int(square):
        if number % divider == 0:
            return False
        divider += 1
    return True

# print(prime_factorization(20))
# print(prime_or_not(19))
