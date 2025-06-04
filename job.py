gender=input("Enter gender:")
if gender == "Male"
    score = float(input("Enter score:"))
    if score>60:
        region = input("Enter region:")
        if region=="local":
            print("eligible")
        else:
            print("not eligible")
else:
    print("not eligible")
