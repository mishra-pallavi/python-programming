# Reversing a List in Python

# Example: 
# Input: list = [4, 5, 6, 7, 8, 9]
# Output: [9, 8, 7, 6, 5, 4] 
# Explanation: The list we are having in the output is reversed to the list we have in the input.

# Below are the approaches to reverse a list:

# Using the slicing technique
# Reversing list by swapping present and last numbers at a time
# Using the reversed() and reverse() built-in function
# Using a two-pointer approach
# Using the insert() function
# Using list comprehension
# Reversing a list using Numpy

#1 : Reverse Array using the slicing
def Reverse(lst):
    new_list = lst[::-1]
    return new_list

lst = [10, 11, 12, 13, 14, 15]
print("Original List : ",lst)
print("Reversed List ",Reverse(lst))