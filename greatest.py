n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))
n3=int(input("Enter 3rd number:"))
n4=int(input("Enter 4th number:"))
if n1>n2 and n1>n3 and n1>n4:
    print(f"{n1} is greatest")
elif n2>n1 and n2>n3 and n2>n4:
    print(f"{n2} is greatest")
elif n3>n1 and n3>n2 and n3>n4:
    print(f"{n3} is greatest")
else:
    print(f"{n4} is greatest")
