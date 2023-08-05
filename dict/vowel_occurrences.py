# Write a program to find number of occurrences of each vowel present in the given string?
mystr = input("Input a string : ")
vowels = {'a','e','i','o','u'}
d = {}
for i in mystr:
    if i in vowels:
        d[i] = d.get(i,0)+1
for k,v in sorted(d.items()):
    print(k, "occured ", v, " times")