# The formula to calculate compound interest annually is given by: 

# A = P(1 + R/100) t 

# Compound Interest = A – P 
# A is amount and P is the principal amount and R is the rate and T is the time span

def compound_interest(principal, rate, time):
    amount = principal * pow((1+rate/100),time)
    CI = amount - principal
    print(f"Compound intrest is {CI}")


compound_interest(1000,5,2)


## Compound Interest with Input taking from user

principal = int(input("Enter the principle amount: "))
rate = int(input("Enter rate of interest : "))
time = int(input("Enter time is years : "))
compound_interest(principal,rate,time)

## Finding compound interest of given values without using pow() function.

p= 1200   # principal amount 
t= 2      # time 
r= 5.4    # rate 
a = p*(1+r/100)**t
ci = a-p
print(f"compond interest = {ci}") 



## Compound Interest using for loop

def compond_interest_loop(p,r,t):
    amount = p
    for i in range(t):
        amount = amount * (1+r/100)
    ci = amount-p
    print(f"Compound interest usinf foor loop is {ci}")

compond_interest_loop(12000,5.4,2)