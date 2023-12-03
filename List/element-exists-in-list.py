# Check if element exists in list in Python

# Input: test_list = [1, 6, 3, 5, 3, 4]
#             3  # Check if 3 exist or not.
# Output: True
# Explanation: The output is True because the element we are looking is exist in the list.

## Check if an element exists in a list in Python

# Using “in” Statement 
# Using a loop 
# Using any() function
# Using count() function
# Using sort with bisect_left and set()
# Using find() method
# Using Counter() function
# Using try-except block


#1 : Check if an element exists in the list using the “in” statement



lst=[ 1, 6, 3, 5, 3, 4 ] 

i=7

if i in lst:
    print(f"{i} Exist in given list")
else:
    print(f"{i} not exist in given list")


#2 : Find if an element exists in the list using a loop 

lst=[ 1, 6, 3, 5, 3, 4 ] 

find=5

for i in lst:
    if i == find:
        print(f"{find} Exist in given list")

#3 : Check if an element exists in the list using any() function

test_list = [1, 6, 3, 5, 3, 4]

result = any(item in test_list for item in test_list)
print("Does string contain any list element : " +str(bool(result)))

#4 : Find if an element exists in the list using the count() function
test_list = [10, 15, 20, 7, 46, 2808]
 
print("Checking if 15 exists in list")

exist_count = test_list.count(15)
if exist_count > 0:
    print("Yes, 15 exist in list")
else:
    print("No, 15 does not exist in list")
