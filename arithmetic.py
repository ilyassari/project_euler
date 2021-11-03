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

""" Greatest Common Divisor and Least Common Multiple """

def gcd(*numbers):
    """ take numbers as integers or as one list or one tuple;
        return greatest common divisor"""
    if isinstance(numbers[0], (list, tuple)):
        numbers = numbers[0]
    result = 1
    numbers = list(numbers)
    max_number = max(numbers)
    primes = prime_list(max_number + 1)
    while any(x != 1 for x in numbers):
        for prime in primes:
            while any(x % prime == 0 for x in numbers):
                temp = numbers.copy()
                for i in range(len(numbers)):
                    if numbers[i] % prime == 0:
                        numbers[i] /= prime
                if all(int(numbers[i]) != int(temp[i]) for i in range(len(numbers))):
                    result *= prime
    return result

def lcm(*numbers):
    """ take numbers as integers or as one list or one tuple;
        return least common multiple"""
    if isinstance(numbers[0], (list, tuple)):
        numbers = numbers[0]
    result = 1
    numbers = list(numbers)
    max_number = max(numbers)
    primes = prime_list(max_number + 1)
    while any(x != 1 for x in numbers):
        for prime in primes:
            while any(x % prime == 0 for x in numbers):
                temp = numbers.copy()
                for i in range(len(numbers)):
                    if numbers[i] % prime == 0:
                        numbers[i] /= prime
                if numbers != temp:
                    result *= prime
    return result
