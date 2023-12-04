# clear a list in Python

# Example
# Input: [2, 3, 5, 6, 7]
# Output: []
# Explanation: Python list is cleared and it becomes empty so we have returned empty list.

# Different Ways to Remove from a List in Python
# Using clear()
# Reinitializing the list
# Using “*= 0”
# Using del
# Using pop() method
# Using slicing

#1 :  Clear a List using Python List clear()

lst = [6, 0, 4, 1]
print('List before clear:', lst)
 
# Clearing list
lst.clear()
print('GEEK after clear:', lst)


#2 : Clear a List by Reinitializing the List

lst = [6, 0, 4, 1]
print("List before deleting is : ",lst)

lst = []
print("List after clearing using reinitialization : ",lst )

#3 :  Clearing a Python List Using “*= 0”

lst = [1,2,3,4,5]
print("List before clearing is : ",lst)

lst*=0
print("List after clearing using *=0 : ",lst )

#4 : Clearing a List Using del

list1 = [1, 2, 3]
list2 = [5, 6, 7]

print("List1 before deleting is ",list1)

del list1[:]
print("List1 After deleting using del ",list1)

print("List2 before deleting is ",list2)

del list2[:]
print("List2 After deleting using del ",list2)


#5 : Python pop() method To Clear a List

list1 = [1, 2, 3]

print("List1 before deleting is ",list1)

while(len(list1) != 0):
    list1.pop()

print("List1 after clearing using pop is ",list1)

#6 : Clear a List using Slicing

lst = [1, 2, 3, 4, 5]
 
print("List before clearing: ",lst)

lst = lst[:0]

print("List after clearing using Slicing: ",lst)