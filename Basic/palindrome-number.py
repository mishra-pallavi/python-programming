def palindrome(n):
    temp = n
    res = 0
    while n >0:
        dig = n%10
        res = res*10+dig
        n=n//10
    if res == temp:
        return True
    else:
        return False 

n = 12222
print(palindrome(n))