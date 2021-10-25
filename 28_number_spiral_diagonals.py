'''
Problem 28 Number spiral diagonals

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

            _21_22 23 24_25_
             20 _7_ 8 _9_10
             19  6 _1_ 2 11
             18 _5_ 4 _3_12
            _17_16 15 14_13_

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

def zero_matrice(row, col):
    "take row and column number return all zero matrice"
    matrice = list()
    for _ in range(row):
        matrice.append(list())
        for __ in range(col):
            matrice[-1].append(0)
    return matrice

def spiral_matrice(n):
    "take row (= column) number return a spirally filled matrice "
    # make all zero matrice
    matrice = zero_matrice(n + 2, n + 2)
        #add extra 2 rows and columns to write number properly
    # focus on center point
    row = int((n + 1) / 2)
    col = int((n + 1) / 2)
    # write numbers in matrice
    for num in range(1, (n * n) + 1):
        matrice[row][col] = num
        # decide next location
        if matrice[row][col + 1] != 0 and matrice[row - 1][col] == 0:
            row -= 1
        elif matrice[row - 1][col] != 0 and matrice[row][col - 1] == 0:
            col -= 1
        elif matrice[row][col - 1] != 0 and matrice[row + 1][col] == 0:
            row += 1
        else:
            col += 1
    # remove extra rows and columns
    del matrice[0]
    del matrice[-1]
    for i in range(len(matrice)):
        del matrice[i][0]
        del matrice[i][-1]
    return matrice

def diagonal_sum(matrice):
    "take square matrice return sum of diagonal numbers"
    sum =- 1
    for i in range(len(matrice)):
        sum += matrice[i][i]
        sum += matrice[i][-i-1]
    return sum

print(diagonal_sum(spiral_matrice(1001))) #669171001
