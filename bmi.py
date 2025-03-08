'''The body mass index (BMI) was created by a Belgian mathematician in the 1850s and it's used by health and nutrition professionals to estimate human body fat in certain populations.
It is computed by taking an individual's weight (mass) in kilograms and dividing it by the square of their height in meters.
bmi=mass/height^2 
​Create a bmi.py program that calculates your own BMI.'''

mass=int(input("Enter mass in kg")) 
height=int(input("Enter height in cm"))
height = height / 100  
bmi=mass/height**2
print("The body mass index is",bmi)
