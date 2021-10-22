import math

""" Direct math functions """
def factorial(n):
    return (math.factorial(n))

def sqrt(n):
    return (math.sqrt(n))


""" NOT CLASSIFIED """

def all_factors(number):
    """ take a number; return its all factors as a list"""
    divider = 2
    factors = [1]
    while divider <= number / 2:
        if number % divider == 0:
            factors.append(divider)
        divider += 1
    return factors

def find_root(number, exp, decimal):
    num = 0
    number *= 10 ** (decimal * exp)
    while num ** exp < number:
        num += 1
    return num / 10 ** decimal

""" PRIME NUMBERS """

def prime_factorization(number):
    """ take a number; return its all prime factors as a list"""
    divider = 2
    prime_factors = list()
    while divider <= number:
        while number % divider == 0:
            number = number / divider
            prime_factors.append(divider)
        divider += 1
    return prime_factors

def prime_or_not(number):
    """take a number; return its prime or not as boolean"""
    if number == 1:
        return False
    divider = 2
    while divider <= int(sqrt(number)):
        if number % divider == 0:
            return False
        divider += 1
    return True

def prime_list(boundary):
    """ take a number return a list of prime numbers under number """
    numbers = list(range(2, boundary))
    for num in numbers:
        for check in numbers:
            if check != num and check % num == 0:
                numbers.remove(check)
    return numbers
