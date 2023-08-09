greet = lambda : print("Hello")

greet()

greet1 = lambda name : print("hello ",name)

greet1("pallavi")

# Q. Write a program to create a lambda function to find square of given number?
sqr = lambda n: print(n*n)
sqr(4) 

# Q. Lambda function to find sum of 2 given numbers
sum = lambda a,b: print(a+b)
sum(10,20)

# Q. Lambda Function to find biggest of given values.
big = lambda a,b: a if a>b else b
print(big(10,20))

# Q. Program to filter only even numbers from the list by using filter() function?
l=[0,5,10,15,20,25,30]
l1 = list(filter(lambda x: x%2 == 0,l))
print(l1)

l2 = list(filter(lambda x: x%2 != 0, l))
print(l2)

# map double the given list element
a=[1,2,3,4,5]
a1 = list(map(lambda x: x*2, a))
print(a1)

# Eg 2: To find square of given numbers
b=[1,2,3,4,5]
b1 = list(map(lambda x: x*x, b))
print(b1)

# apply map on 2 list
l1=[1,2,3,4]
l2=[2,3,4,5]
l3 = list(map(lambda x,y:x*y,l1,l2))
print(l3)
#[2, 6, 12, 20]