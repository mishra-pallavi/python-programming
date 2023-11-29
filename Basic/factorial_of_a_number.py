# Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. 

## Find the Factorial of a Number Using Recursive approach

def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)

num = 5
print(f"Factorial of {num} is {factorial(num)}")


## Find the Factorial of a Number Using Iterative approach

def factorial_iter(num):
    if num < 0:
        return 0
    elif num == 0 or num == 1:
        return 1
    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
    return fact

num = 5
print(f"Factorial of {num} is {factorial_iter(num)}")    


## Find the Factorial of a Number Using One line Solution (Using Ternary operator): 

def factorial_ternary(n):
    return 1 if (n==1 or n==0) else n*factorial_ternary(n-1)

num = 5
print(f"Factorial of {num} is {factorial_ternary(num)}")    


## Find the Factorial of a Number Using using In-built function 

import math

def factorial_m(n):
    return (math.factorial(n))

num = 5
print("Factorial of", num, "is",
      factorial(num))

