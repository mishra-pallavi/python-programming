## Find Maximum of two numbers in Python

# This is the naive approach where we will compare two numbers using if-else statement and will print the output accordingly.

def maximum(a,b):
    if a >= b:
        return a
    else:
        return b
    
num1 = 10
num2 = 20

max = maximum(num1,num2)
print(f"Maximum of {num1} and {num2} is {max}")


## Find Maximum of two numbers Using max() function

a = 4
b = 2

# result = max(a, b)

# print(f"using max operation: the max between {a} and {b} is {result}")


## Maximum of two numbers Using Ternary Operator

a = 2
b = 4
print(f"using ternary operation the max between {a} and {b} is {a if a >= b else b}")


## Maximum of two numbers Using lambda function 

a = 2;b =4
maxnum = lambda a,b:a if a >= b else b
print(f'{maxnum(a,b)} is a maximum number')


## Maximum of two numbers Using list comprehension

a = 2;b=4
x = [a if a >= b else b]
print(f"max number is {x}")  

# Maximum of two numbers Using sort() method

a = 2;b = 4
x = [a,b]
x.sort()
print(x[-1])
