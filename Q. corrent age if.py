currentyear=int(input("enter the current year"))
birthyear=int(input("enter the birth year"))
if currentyear>birthyear:
    print(currentyear-birthyear)
elif birthyear>currentyear:
    print(birthyear-currentyear)
else:
    print("error")

