name = input("Enter string/name : ")

# strlist = name.split()

# reverceStr = [strlist[::-1] for strlist in strlist]

# updated_str = " ".join(reverceStr)
# print(updated_str)

reversed_string = name[::-1]
print(reversed_string)

# 2nd method using join and reversed function
print("".join(reversed(name)))

# 3rd method using while loop
i = len(name)-1
target=''
while i>=0:
    target = target+name[i]
    i=i-1
print(target)