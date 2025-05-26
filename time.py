import time
time=time.strftime("%H:%M:%S")
print(time)
if (time>="06:00:00")and (time<="11:59:00"):
    print("Good Morning")
elif (time>="12:00:00") and (time<="17:59:00"):
    print("Good Afternoon")
elif (time>="18:00:00")and(time<="23:59:00"):
    print("good evening!")
else:
    print("Good Night!")
