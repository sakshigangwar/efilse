num=int(input("enter the number"))
if num%2!=0 and num%3!=0 and num%5!=0:
    print("it is a prime number")
elif num==2 or num==3 or num==5:
    print("it is also prime number")
else:
    print("it is not prime")


