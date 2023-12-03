# Python Program for Array Rotation Using temp array

# Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
# 1) Store d elements in a temp array
#    temp[] = [1, 2]
# 2) Shift rest of the arr[]
#    arr[] = [3, 4, 5, 6, 7, 6, 7]
# 3) Store back the d elements
#    arr[] = [3, 4, 5, 6, 7, 1, 2]


def rotateArr(arr,d,n):
    temp = []
    i = 0
    while i < d:
        temp.append(arr[i])
        i = i+1
    
    i = 0
    while d < n:
        arr[i] = arr[d]
        i = i +1
        d = d + 1

    arr[:] = arr[: i]+temp
    return arr


arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
res = rotateArr(arr,d,n)
print(res)



## Python Program for Reversal Algorithm of Array Rotation
def rverseArray(arr,d):
    c = (arr[d:]+arr[:d])
    return c

arr = [1, 2, 3, 4, 5, 6, 7]
d=2
print(rverseArray(arr,d))