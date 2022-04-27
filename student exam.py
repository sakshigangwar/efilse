classheld=int(input("enter the classheld"))
classattened=int(input("enter the classattened"))
percentage=classattened/classheld*100
if percentage>=75:
    print("you can sit for the exam",int(percentage))
elif percentage<=75:
    print("you can not sit for the exam",int(percentage))
else:
    print("drop out")