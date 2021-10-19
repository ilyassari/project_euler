'''
Problem 10 Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

from aritmetic import prime_or_not

def sum_primes(boundary):
    total = 2 #2 is the first prime number
    for i in range(3, boundary, 2):
        if prime_or_not(i):
            total += i
    return total

print(f"toplam: {sum_primes(2000000)}") #142913828922
