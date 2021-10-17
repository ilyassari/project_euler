'''
Problem 7 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''
from primes import prime_or_not

def nst_prime(order):
    prime_order = 1
    number = 0
    while prime_order <= order:
        number += 1
        if prime_or_not(number):
            prime_order += 1
    return number

print(nst_prime(10001)) #104743
