'''
Problem 9 Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
        a^2 + b^2 = c^2
        
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def pthTrip(total):
    for a in range (total):
        for b in range (a + 1):
            if a ** 2 + b ** 2 == (total - a - b) ** 2:
                return f"""numbers are {a}, {b}, {(total - a - b)}; and product is {(a * b * (total - a - b))}"""

print(pthTrip(1000))
