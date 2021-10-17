'''
Problem 6 Sum square difference

The sum of the squares of the first ten natural numbers is,
        1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
        (1+2+...+10)^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sum_exp_dif(boundary, exp):
    sum_exps = 0 #totals of exp
    exp_sum = 0 #exp of total
    for i in range(1, boundary + 1):
        sum_exps += i ** exp
        exp_sum += i
    exp_sum = exp_sum ** exp
    return exp_sum - sum_exps

print(sum_exp_dif(100, 2)) #25164150
