'''Problem 18 Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

'''


test0 = """3
7 4
2 4 6
8 5 9 3"""

test1 = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''


def make_list(string):
    """ take list as string give as list"""
    numbers = string.split('\n')
    for i in range(len(numbers)):
        numbers[i] = numbers[i].split(' ')
        for j in range(len(numbers[i])):
            numbers[i][j] = int(numbers[i][j])
    return numbers

def route_list_extender(routes):
    """ take route list and give double """
    temp = routes.copy()
    for route in temp:
        routes.append(list())
        for number in route:
            routes[-1].append(number)
    return routes

def create_routes(step):
    """ take step count and give route list """
    routes = [[0]]
    for i in range(1, step):
        routes = route_list_extender(routes)
        for j in range(int(len(routes) / 2)):
            routes[j].append(routes[j][-1])
        for j in range(int(len(routes) / 2), len(routes)):
            routes[j].append(routes[j][-1] + 1)
    return routes

def max_sum(numbers, routes):
    result = 0
    for route in routes: #[0, 0, 0, 0, 0, 0, 0]
        values = list() # The list created by reading the values in numbers for each route
        for step in range(len(route)):
            values.append(numbers[step][route[step]])
        result = max(sum(values), result)
    return result

numbers = make_list(test1)
print(max_sum(numbers, create_routes(len(numbers)))) #1074
