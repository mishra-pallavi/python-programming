# Program to Print all Prime numbers in an Interval

def prime(start,end):
    prime_list = []
    for i in range(start,end):
        if i==0 or i==1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i % j == 0:
                    break
                else:
                    prime_list.append(i)

    return prime_list

start = 2
end = 7
prime_numbers = prime(start,end)
print(prime_numbers)
