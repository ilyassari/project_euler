'''
Problem 27 Quadratic primes

Euler discovered the remarkable quadratic formula:

                    n + n^2 + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39.
However, when n = 40, 40^2 + 40 + 41 = 40 (40 + 1) + 41, is divisible by 41, and certainly when
n = 41, 41^2 + 41 +41 is clearly divisible by 41.

The incredible formula n^2 - 79 n + 1601 was discovered, which produces 80 primes for the consecutive values
0 <= n <= 79.  The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n^2 + an + b, where and |a| < 1000 and |b| <= 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''

from arithmetic import prime_or_not

def prime_number(a, b):
    n = 0
    while True:
        if (n ** 2) + (a * n) + b > 0:
            if prime_or_not((n ** 2) + (a * n) + b):
                n += 1
            else:
                return n
        else:
            return 0

def abs_range(n):
    return list(range(-n, 0)) + list(range(1, n + 1))

def quadratic_primes(max_a, max_b):
    storage = {
        "number": 0
    }
    for a in abs_range(max_a):
        for b in abs_range(max_b):
            if storage["number"] < prime_number(a, b):
                storage["a"] = a
                storage["b"] = b
                storage["number"] = prime_number(a, b)
    return storage

def product_dict(dict):
    return f"a = {dict['a']}, b = {dict['b']} so product is {dict['a'] * dict['b']}"

print(product_dict(quadratic_primes(1000, 1000)))
