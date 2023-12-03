# Find the Length of a List in Python

# Below are the methods or Approach to find the length of a list:

# Using len() function
# Using Naive Method
# Using length_hint()
# Using sum() method
# Using a list comprehension
# Using recursion
# Using enumerate function
# Using Collections Module
# Performance Analysis – Naive vs Python len() vs Python length_hint()

## Approach #1 Using len() function

li = [10, 20, 30]
n = len(li)
print("The length of list is: ", n)


## Approach #2 Using Python Naive Method

test_list = [1, 4, 5, 7, 8]
print("The list is : " + str(test_list))

counter = 0
for i in test_list:
    counter += 1

print("Length of list using naive method is : " + str(counter))

