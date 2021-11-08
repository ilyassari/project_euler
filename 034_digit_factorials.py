"""
Problem 34 Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

from arithmetic import factorial
from stopwatch import stopwatch

def is_curious(number:int):
    """ take number return if it was curious or not """
    if len(str(number)) == 1:
        return False
    sum_fd = 0
    for digit in str(number):
        sum_fd += factorial(int(digit))
    if number == sum_fd:
        return True
    return False

def boundary():
    """Find theory for upper boundary"""
    return 1000000

@stopwatch
def sum_curious():
    """return sum of curious numbers """
    return sum(list(filter(lambda x: is_curious(x), range(boundary()))))

print(sum_curious()) #40730
