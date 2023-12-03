
def findremainder(arr,l,n):
    p = 1
    for i in range(l):
        p = p*arr[i]
    return p % n

arr = [100, 10, 5, 25, 35, 14]
len = len(arr)
n = 11
print(findremainder(arr, len, n))