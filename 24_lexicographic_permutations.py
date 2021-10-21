'''
Problem 24 Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

from arithmetic import factorial

def lexi_perm(digits, order):
    """ takes digits as list and order as integer return a permutation in orderth """
    result = list()
    digits.sort()
    counter = 0
    for _ in range(len(digits)):
        """each loop will delete an element from digit and add to result  """
        fact = factorial(len(digits) - 1
        # fact is the count of permutation if one element of digit selected
        counter += fact
        for i in range(len(digits)):
            if counter >= order:
                #if i is the next number in result
                result.append(digits[i])
                counter -= fact
                break
            else:
                #if i is not the next number in result; try next i
                counter += fact
        digits.remove(result[-1])
    return result

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
order = 1000000
print(lexi_perm(digits, order)) #[2, 7, 8, 3, 9, 1, 5, 4, 6, 0]
