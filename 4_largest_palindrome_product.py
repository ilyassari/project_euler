'''
Problem 4 Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def check_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False

def palin_n_digit(n, m):
    largest_palindrome = 0
    for i in range(10**(n-1),10**n):
        for j in range(10**(m-1),10**m):
            product = i * j
            if check_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
                prime1, prime2 = i, j
    return (f'{prime1} × {prime2} = {largest_palindrome}')

print(palin_n_digit(3, 3))
