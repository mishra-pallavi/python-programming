# Simple program to add two numbers 

num1 = 15
num2 = 12

sum = num1 + num2
print(f"Sum of {num1} and {num2} is {sum}")

# Adding two numbers with user input

num1 = int(input("Enter first number : "))
num2 = int(input("ENter secound number : "))

sum = num1+num2
print(f"Sum of {num1} and {num2} is {sum}")


# Defining add function and returning the result

def add(a,b):
    return a+b

num1 = 100
num2 = 50

sum = add(num1,num2)
print(f"usigin function : Sum of {num1} and {num2} is {sum}")


# Add two numbers in Python using operator.add() method
num1 = 10
num2 = 15

import operator
sum = operator.add(num1,num2)

print(f"using operator : sum of {num1} and {num2} is {sum}")


# Adding two number using lambda function

add_numbers = lambda x,y: x+y
num1 = 1
num2 = 2

result = add_numbers(num1,num2)
print(f"using lambda function : The sum of {num1} and {num2} is {result}")


# Python program to add two numbers with recursive function

def add_number_recursive(x, y):
    if y == 0:
        return x
    else:
        return add_number_recursive(x+1,y-1)
    
num1 = 5
num2 = 5
result = add_number_recursive(num1,num2)
print(f"using recursive: the sum of {num1} and {num2} is {result}")


