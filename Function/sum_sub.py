# returnig multiple value from a function
def sum_sub(a,b):
    sum = a+b
    sub = a-b
    return sum,sub


num1 = eval(input("enter num1 : "))
num2 = eval(input("enter num2 : "))
sum,sub = sum_sub(num1,num2)
print(f"sum of {num1},{num2} is {sum}")
print(f"sub of {num1},{num2} is {sub}")