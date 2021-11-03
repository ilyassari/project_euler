'''
Problem 3 Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

def l_prime_factor(number):
    factor = 2
    while factor < number:
        while number % factor == 0:
            number /= factor
        if number == 1:
            # if largest prime factor have two or more force
            number = factor
        factor += 1
    return number

q = 600851475143
print(f"Largest prime of {q} is {int(l_prime_factor(q))}") #6857
