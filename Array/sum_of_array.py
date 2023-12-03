# Given an array of integers, find the sum of its elements.

# Input : arr[] = {1, 2, 3}
# Output : 6
# Explanation: 1 + 2 + 3 = 6

def ArrSum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

arr = [12, 3, 4, 15]

result = ArrSum(arr)

print(f"sum of given array is : {result}")



## Program to Find Sum of Array Using sum()



arr = [12, 3, 4, 15,20]

ans = sum(arr)

print(f"Sum of given array is : {ans}")


## Program to Find Sum of Array Using reduce method




## Program to Find Sum of Array Using Divide and conquer

def sum_of_array(arr, low, high):
    if low == high:
        return arr[low]
    
    mid = (low+high)//2
    left_sum = sum_of_array(arr,low,mid)
    right_sum = sum_of_array(arr,mid+1,high)
    return left_sum+right_sum



arr = [1, 2, 3]
print(sum_of_array(arr, 0, len(arr)-1)) # Output: 6
 
arr = [15, 12, 13, 10]
print(sum_of_array(arr, 0, len(arr)-1)) # Output: 50