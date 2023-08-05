def fact(num):
    result = 1
    while num >= 1:
        result = result*num
        num = num-1
    return result

num = eval(input("Enter a number : "))
fact = fact(num)
print(f"Factorial of {num} is {fact}") 