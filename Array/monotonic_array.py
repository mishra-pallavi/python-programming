# Program to check if given array is Monotonic

def isMonotonic(A):
    x,y = [],[]
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    if(x == A or y == A):
        return True
    return False

A = [6, 5, 4, 4]
 
# Print required result
print(isMonotonic(A))


def isMonotonic2(A):
    return (all(A[i] <= A[i+1] for i in range(len(A) - 1)) or (all(A[i] >= A[i+1] for i in range(len(A) -1))))

A = [6, 5, 5, 7]
 
# Print required result
print(isMonotonic2(A))