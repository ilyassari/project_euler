'''
Problem 15 Lattice paths

Starting in the top left corner of a 2 × 2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

        see 015_pic.png

How many such routes are there through a 20 × 20 grid?
'''

from arithmetic import factorial

def lat_path(x, y):
    return factorial(x + y) / (factorial(x) * factorial(y))

print(lat_path(20, 20)) #137846528820
