buy=int(input("enter your amount:"))
if buy>=1000:
    discount=(10/100)*buy
    print("You will get a discount of RS.",discount)
else:
    print("You will not get a discount")





buy=int(input("enter the number:"))
dis=buy*10/100
if buy>=5000:
    print("you will get dis. of =",dis)
    print("and you pay only RS.=",buy-dis)
else:
    print("you will not get discount")
    print("you pay full amount=",buy)


