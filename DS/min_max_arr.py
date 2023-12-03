# Find the minimum and maximum element in an array
arr = [10,40,20,50,70,80]
print(arr)
min = 0
for i in arr:
    if min > i:
        min = i

print(f"Min = {min}")
