'''
Problem 30 Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

def digit_powers(base, exp):
    """ take base and exponent return sum of each digit of base powers """
    digits = list(str(base))
    for i in range(len(digits)):
        digits[i] = int(digits[i]) ** exp
    return sum(digits)

def equal_digit_exp_sum(exp):
    """ take exponent value;
    return sum of numbers which equal to the sum of the exponent of each digit """
    sum = 0
    for num in range(2, 194980): # theoretical upper limit must be calculated
        if num == digit_powers(num, exp):
            print(num)
            sum += num
    return sum

print(f"sum: {equal_digit_exp_sum(5)}") #443839
