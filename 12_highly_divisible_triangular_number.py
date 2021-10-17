'''
Problem 12 Highly divisible triangular number

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

from primes import prime_factorization

def hidivtrinu(n): #çok yavaş
    numbers = [1] # list of triangle numbers
    natural_number = 2
    while True:
        numbers.append(numbers[-1] + natural_number)
        natural_number += 1
        divisor = 1
        all_factors = prime_factorization(numbers[-1])
        factors = list() # prime factors
        exps = list() # force of prime factors
        for item in all_factors:
            if not item in factors:
                factors.append(item)
                exps.append(all_factors.count(item))
        for item in exps:
            divisor *= (item + 1)
        if divisor >= n:
            break
    return numbers[-1]

print(hidivtrinu(500)) #76576500
