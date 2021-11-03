"""
Problem 33 Digit cancelling fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""

from arithmetic import all_factors

# ab / ca  # ba / ac

def curious_fraction(sf, n, d):
    """sf: simplified figure
        n: numerator
        d: denominator
    """
    if ((10 * sf) + n ) / ((10 * d) + sf) == (n / d):
        return True
    elif ((10 * n) + sf ) / ((10 * sf) + d) == (n / d):
        return True
    else:
        return False

def digit_canceler_looper():
    product = {
        "numerator": 1,
        "denominator": 1
    }
    for sf in range(1, 10):
        for d in range(2, sf):
            for n in range(1, d):
                if curious_fraction(sf, n, d):
                    print(f"{n}{sf} / {sf}{d} = {n} / {d}")
                    product["numerator"] *= n
                    product["denominator"] *= d
    simplifiers = all_factors(product["numerator"])
    for number in simplifiers:
        if product["denominator"] % number == 0:
            product["denominator"] /= number
    return product["denominator"]





print(digit_canceler_looper())
