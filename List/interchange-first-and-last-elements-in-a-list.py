# Given a list, write a Python program to swap first and last element of the list.

# Examples: 

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]

## Approach #1: Find the length of the list and simply swap the first element with (n-1)th element.

def swapList(l):
    size = len(l)
    temp = l[0]
    l[0] = l[size-1]
    l[size-1] = temp
    return l

newList = [12, 35, 9, 56, 24]
 
print(swapList(newList))