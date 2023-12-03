# Given a list, write a Python program to swap first and last element of the list.

# Examples: 

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]

## Approach #1: Find the length of the list and simply swap the first element with (n-1)th element. (using temp variable)

def swapList(l):
    size = len(l)
    temp = l[0]
    l[0] = l[size-1]
    l[size-1] = temp
    return l

newList = [12, 35, 9, 56, 24]
print("Original List : ",newList)
print("After interchnage List : ",swapList(newList))


## Approach #2: The last element of the list can be referred as list[-1]. Therefore, we can simply swap list[0] with list[-1].

def swapListTwo(l):
    l[0], l[-1] = l[-1], l[0]
    return l

newList = [1, 2, 3]
print("Original List Approach 2: ",newList)
print("After interchnage List : ",swapListTwo(newList))


## Approach #3: Swap the first and last element is using tuple variable. 
# Store the first and last element as a pair in a tuple variable, say get, 
# and unpack those elements with first and last element in that list. 
# Now, the First and last values in that list are swapped. 

def swapListThree(l):
    get = l[-1],l[0]
    l[0],l[-1] = get
    return l

newList = [12, 35, 9, 56, 24]

print("Original List Approach 3: ",newList)
print("After interchnage List : ",swapListThree(newList))


## Approach #4: Using * operand.

def swapListFour(l):

    start, *middle, end = l
    l = end, *middle, start

    return l

newList = [12, 35, 9, 56, 24]
print("Original List Approach 4: ",newList)
print("After interchnage List : ",swapListFour(newList))


## Approach #5: Swap the first and last elements is to use the inbuilt function list.pop(),  insert() and append.

def swapListFive(l):
    start = l.pop(0)
    end = l.pop(-1)

    l.insert(0,end)
    l.append(start)
    return l

newList = [12, 35, 9, 56, 24]
print("Original List Approach 5: ",newList)
print("After interchnage List : ",swapListFive(newList))
