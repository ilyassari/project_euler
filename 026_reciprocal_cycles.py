'''
Problem 26 Reciprocal cycles

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1 / 2	    = 	0.5
    1 / 3	    = 	0.(3)
    1 / 4	    = 	0.25
    1 / 5	    = 	0.2
    1 / 6	    = 	0.1(6)
    1 / 7	    = 	0.(142857)
    1 / 8	    = 	0.125
    1 / 9	    = 	0.(1)
    1 / 10      = 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

from decimal import Decimal, getcontext

def dec_division(dividend, divisor, length):
    """ take dividend, divisor and decimal length;
    return division as decimal object """
    getcontext().prec = length
    return Decimal(dividend) / Decimal(divisor)

def check_repeats(escrol):
    """ take list; return its recurring part at tail """
    if escrol[0] in escrol[1:]:
        indices = [x for x, d in enumerate(escrol) if d == escrol[0]]
        for i in range(1, int(len(indices) / 3)):
            length = indices[i] - indices[0]
            checklist = list()
            for j in range(1, length + 1):
                check = escrol[j] == escrol[j + length] \
                and escrol[j] == escrol[j + (2 * length)] \
                and escrol[j] == escrol[j + (3 * length)]
                if check:
                    checklist.append(check)
                else:
                    checklist.append(check)
                    break
            if all(checklist):
                return escrol[:length]
        return check_repeats(escrol[1:])
    else:
        return check_repeats(escrol[1:])

def recurring(dividend, divisor, length):
    """ take dividend, divisor and maximum length of decimal;
    return length of recurring part of division """
    dec_number = dec_division(dividend, divisor, length)
    dec_part = list(str(dec_number).split(".")[-1])
    if len(dec_part) < length:
        return 0
    else:
        return len(check_repeats(dec_part))

def reciprocal_cycle(low_bound, upp_bound, length):
    """ take lower and upper boundary and maximum length of decimal;
    return the value under upper boundary for which 1/value contains
    the longest recurring cycle in its decimal fraction part  """
    number = 1
    recurring_length = 0
    for nu in range(low_bound, upp_bound):
        if recurring(1, nu, length) > recurring_length:
            number = nu
            recurring_length = recurring(1, nu, length)
    return f"1 / {number} contains the longest recurring cycle in its decimal fraction part" \
           f"and length is {recurring_length}."

print(reciprocal_cycle(1, 1000, 4000) ) # then it should be rewritten so that it doesn't need "length"
# 1 / 983 contains the longest recurring cycle in its decimal fraction partand length is 982.
