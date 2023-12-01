# Program to Find Area of a Circle
# Area = pi * r2

def CircleArea(r):
    PI = 3.142
    return PI * (r*r)

cricleArea = CircleArea(10)
print(f"Area of circle is {cricleArea}")


## Python Program to Find Area of a Circle With Math library

import math
def area(r):
    area = math.pi*pow(r,2)
    return print(f"Area of circle is : {area}")

area(5)

