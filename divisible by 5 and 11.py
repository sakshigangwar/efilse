num=int(input("enter the number"))
if num%5==0 and num%11==0:
    print("divisible by both")
elif num%5==0:
    print("divisible by 5")
elif num%11==0:
    print("divisible by 11")
else:
    print("nothing")