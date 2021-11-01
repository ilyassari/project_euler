'''
Problem 32 Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

number_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def check_pool(*args, pool: list):
    """ take numbers and digit pool list;
    return if numbers are built by pool list """
    check = list()
    for number in args:
        for digit in str(number):
            check.append(int(digit))
    check.sort()
    if check == pool:
        return True
    return False

def pandigital_product(min_p, max_p, pool):
    """ take min number max number, and pool list;
    return sum of numbers if the integer divisors from the minimum and
    maximum numbers and themselves composed of digits in the pool """
    sum = 0
    min_product = min_p
    max_product = max_p
    for product in range(min_product, max_product + 1):
        for multiplier in range(1, product):
            multiplicand = (product / multiplier)
            if int(multiplicand) == multiplicand:
                if check_pool(product, multiplier, int(multiplicand), pool = pool):
                    sum += product
                    break
    return sum

print(pandigital_product(123, 9876, number_pool)) #45228
