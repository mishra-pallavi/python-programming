# Python program to check whether the string is Symmetrical or Palindrome

def Palindrome(string):

    mid = len(string)/2
    start = 0
    end = len(string)-1
    flag = 0
    while start <= mid:
        if string[start] == string[end]:
            start +=1
            end -=1
        else:
            flag = 1
            break
    if flag == 0:
        print("string is palindrom")
    else:
        print("string is not palindrom")

def Symmetrical(string):
    n = len(string)
    flag = 0

    if n%2==0:
        mid = n//2+1
    else:
        mid = n//2

    start1 = 0
    start2 = mid

    while(start1 < mid and start2 < n):
        if(string[start1] == string[start2]):
            start1 = start1+1
            start2 = start2+1
        else:
            flag = 1
            break

    if flag == 1:
        print("String is Symmetrical")
    else:
        print("String is not Symmetrical")
    
    return
s = 'khokho'
Palindrome(s)
Symmetrical(s)
