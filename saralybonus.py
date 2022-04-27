saraly=int(input("enter the saraly"))
serviceyear=int(input("enter the year"))
bonus=(saraly/100*5)
if serviceyear>=5:
    print(saraly+bonus)
else:
    print("you have work less than 5 year so you will get only",saraly)

