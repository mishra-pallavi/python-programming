# Python Program for Simple Interest

# Simple Interest = (P x T x R)/100 Where, P is the principal amount T is the time and R is the rate

def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
    si = (p*t*r)/10
    print('Simple intrest is : ',si)

simple_interest(1000,6,5)


## Program for simple interest with Taking input from user

p = int(input("Plase Enter principle : "))
t = int(input("Please enter tenure : "))
r = int(input("Please enter rate : "))
simple_interest(p,t,r)
