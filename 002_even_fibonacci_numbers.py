'''
Problem 2   Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def fibonacci_total(boundary):
    all_fib_nums = [1, 2]
    while all_fib_nums[-1] <= boundary:
        all_fib_nums.append(all_fib_nums[-2] + all_fib_nums[-1])
    return sum(list(filter(lambda item: item % 2 == 0, all_fib_nums)))

print(f'Evens Total: {fibonacci_total(4000000)}')     #4613732