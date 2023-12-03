# Given a list in Python and provided the positions of the elements, write a program to swap the two elements 
# in the list. 

# Examples:  

# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

# Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output : [1, 5, 3, 4, 2]

## Approach #1 Swap Two Elements in a List using comma assignment 
def swapPositions(l,pos1,pos2):
    l[pos1], l[pos2] = l[pos2], l[pos1]
    return l

List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
print("Original List Approach 1: ",List)
print("After interchnage List : ",swapPositions(List, pos1-1, pos2-1))


## Approach #2 Using Inbuilt list.pop() function to Swap Two Elements in a List

def swapPositionsTwo(l,pos1,pos2):
    first = l.pop(pos1)
    secound = l.pop(pos2-1)
    l.insert(pos1,secound)
    l.insert(pos2,first)
    return l

List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
print("Original List Approach 2: ",List)
print("After interchnage List : ",swapPositionsTwo(List, pos1-1, pos2-1))



## Approach #3 Swap Two Elements in a List Using tuple variable

def swapPositionsThree(l,pos1,pos2):
    get = l[pos1],l[pos2]
    l[pos2],l[pos1] = get    
    return l


List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
print("Original List Approach 3: ",List)
print("After interchnage List : ",swapPositionsThree(List, pos1-1, pos2-1))


## Approach #5 Swap Two Elements in a List Using temp variable

def swapPositionsFour(l,pos1,pos2):
    temp = l[pos1]
    l[pos1] = l[pos2]
    l[pos2] = temp
    return l

List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
print("Original List Approach 5: ",List)
print("After interchnage List : ",swapPositionsFour(List, pos1-1, pos2-1))

## Approach #4 Swap Two Elements in a List Using enumerate

def swapPositionsFive(l,pos1,pos2):
    for i , x in enumerate(l):
        if i == pos1:
            elem1 = x
        if i == pos2:
            elem2 = x
    l[pos1] = elem2
    l[pos2] = elem1
    return l

List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
print("Original List Approach 4: ",List)
print("After interchnage List : ",swapPositionsFive(List, pos1-1, pos2-1))

