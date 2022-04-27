classheld=int(input("enter the number"))
classattend=int(input("enter the number"))
percentage=(classattend/classheld*100)
if percentage>=75:
    print("you are allow sit the exam",percentage)
elif percentage<=75:
    print("you are not allow sit the exam",percentage)
else:
    print("will not sit for exam")