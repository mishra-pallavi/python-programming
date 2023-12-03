# Program to Find Largest Element in an Array

# Find largest element in an array Using Native Approach

def largest(arr):
    n = len(arr)
    max=arr[0]
    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [10,20,34,67,4,13,70]
res = largest(arr)
print(f"Largest element of given array is : {res}")


## Find largest element in an array Using built-in function max()

def largestMax(arr):
    res = max(arr)
    return res

arr = [10,20,34,67,4,130,70]
res = largest(arr)
print(f"Largest element of given array is : {res}")



## Find largest element in an array Using sort() function
def largest_element(arr,n):
    arr.sort()

    return arr[n-1]



arr = [10,20,34,67,4,130,70]
n = len(arr)
res = largest_element(arr,n)
print(f"Largest element is : {res}")


## Find largest element in an array Using reduce() function
from functools import reduce

def largest(arr):
    result = reduce(max, arr)
    return result


arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr)
print("Largest in given array ", Ans)


## Find Largest Element with Python Lambda

arr = [10, 324, 45, 90, 98]
largest_element = max(arr, key=lambda x:x)
print("Largest element in given array ", largest_element)


