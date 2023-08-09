def checknumber(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

num = eval(input("Enter a number to check : "))
checknumber(num)