s1 = input("Enter First string : ")
s2 = input("Enter secound string : ")
output = ''
i,j = 0,0
while i < len(s1) or j < len(s2):
    if i < len(s1):
        output = output+s1[i]
        i+=1
    if j < len(s2):
        output = output+s2[j]
        j+=1
print(output)