# Program to check Armstrong Number

def order(x):
    n = 0
    while x != 0:
        n = n + 1
        x = x // 10
    return n

def power(r,n):
    if n ==0:
        return 1
    if n%2 == 0:
        return power(r,n // 2)*power(r,n // 2)
    
    return r * power(r,n //2)*power(r,n //2)
    


def isArmstrong(x):
    n = order(x)
    temp = x
    sum1 = 0

    while temp != 0:
        r = temp % 10
        sum1 = sum1 + power(r,n)
        temp = temp // 10
    
    return (sum1 == x)

num = 153
print(isArmstrong(num))

num = 1253
print(isArmstrong(num))