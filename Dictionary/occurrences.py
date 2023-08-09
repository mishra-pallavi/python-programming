# Q. Write a program to find number of occurrences of each letter present in the given string?
my_str = input("Enter a string : ")
print(my_str)
d={}
for i in my_str:
    d[i] = d.get(i,0)+1

for k,v in d.items():
    print(k,"occured ",v, "times")
print(d)