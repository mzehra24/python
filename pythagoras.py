#Create a hypotenuse.py program that asks the user for two numbers, a and b, and then calculates the hypotenuse c.

import math
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=math.sqrt(a**2+b**2)
print("The hypotenose is",c)
