# Q. Write a program to accept student name and marks from the keyboard and creates a dictionary. Also display student marks by taking student name as input?
num = int(input("enter no of students : "))
d = {}
for i in range(num):
    name = input(f"enter {i} student name : ")
    marks = input(f"enter {i} student marks : ")
    d[name] = marks
while True:
    name = input("enter name your want marks : ")
    marks = d.get(name,-1)
    if marks == -1:
        print("Student not found")
    else:
        print("Marks of", name, " are ", marks)
    option= input("do you want more student marks[yes/no]")
    if option == 'no':
        break