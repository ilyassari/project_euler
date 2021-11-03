'''
Problem 31 Coin sums

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
'''

coins = [1, 2, 5, 10, 20, 50, 100, 200]
goal = 200

def different_possibility(values: list, goal: int):
    values.sort()
    values.reverse()
    max_qty = list(map(lambda x: int(goal / x) , values))
    qty = [0] * len(values)
    result = 0
    for qty[0] in range(max_qty[0] + 1):
        total = 0
        total += qty[0]
        if total > goal:
            break
        for qty[1] in range(max_qty[1] + 1):
            total = qty[0]*coins[0]
            total += qty[1]
            if total > goal:
                break
            for qty[2] in range(max_qty[2] + 1):
                total = qty[0] * coins[0] + qty[1] * coins[1]
                total += qty[2]
                if total > goal:
                    break
                for qty[3] in range(max_qty[3] + 1):
                    total = qty[0] * coins[0] + qty[1] * coins[1] + qty[2] * coins[2]
                    total += qty[3]
                    if total > goal:
                        break
                    for qty[4] in range(max_qty[4]+1):
                        total = qty[0] * coins[0] + qty[1] * coins[1] + qty[2] * coins[2] \
                        + qty[3]*coins[3]
                        total += qty[4]
                        if total > goal:
                            break
                        for qty[5] in range(max_qty[5]+1):
                            total = qty[0] * coins[0] + qty[1] * coins[1] + qty[2] * coins[2] \
                            + qty[3] * coins[3] + qty[4] * coins[4]
                            total += qty[5]
                            if total > goal:
                                break
                            for qty[6] in range(max_qty[6] + 1):
                                total = qty[0] * coins[0] + qty[1] * coins[1] + qty[2] * coins[2] \
                                + qty[3] * coins[3] + qty[4] * coins[4] +qty[5] * coins[5]
                                total += qty[6]
                                if total > goal:
                                    break
                                for qty[7] in range(max_qty[7] + 1):
                                    total = qty[0] * coins[0] + qty[1] * coins[1] + qty[2] * coins[2] \
                                    + qty[3] * coins[3] + qty[4] * coins[4] + qty[5] * coins[5] \
                                    + qty[6] * coins[6]
                                    total += qty[7]
                                    if total > goal:
                                        break
                                    if total == goal:
                                        result += 1
    return result

print(different_possibility(coins, goal)) #73682
# it only works for lists of 8 lengths. should be developed to work for lists of different lengths.
