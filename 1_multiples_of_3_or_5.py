'''
Problem 1   Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def multip_sum(*args, boundary):
    sum = 0
    for i in range(1, boundary):
        if any(i % arg == 0 for arg in args):
            sum += i
    return sum

print(multip_sum(3, 5, boundary = 1000)) # 233168
