'''
Problem 5 Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from aritmetic import prime_factorization

def s_multiple(boundary):
    multiple = 1
    primes = list()
    for i in range(2, boundary + 1):
        primes_i = prime_factorization(i)
        for prime in primes_i:
            difference = primes_i.count(prime) - primes.count(prime)
            if difference > 0:
                primes.extend([prime for _ in range(difference)])
    for prime in primes:
        multiple *= prime
    return multiple

print(s_multiple(20))   #232792560
