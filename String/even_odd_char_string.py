# 1st way
# s = input("Enter a string : ")
# print("characters at even positions:",s[0::2])
# print("characters at odd positions:",s[1::2])

# 2nd way
s = input("Enter a string : ")
i = 0
print("CHaracters at even position :")
while i < len(s):
    print(s[i],end=',')
    i=i+2
print()
print("characters at odd position")
i=1
while i < len(s):
    print(s[i],end=',')
    i=i+2