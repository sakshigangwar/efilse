name=input("enter the name")
if  "ing" in name:
    print (name+"ly")
elif "ly" in name :
    print(name + "ing")
else:
    print(name + "ingly")




string=input("enter the string")
if "ly" in string:
    a=string.replace ("ly", "ing")
    print(a)
elif "ing" in string:
    b=string.replace ("ing","ly")
    print(b)
else:
    c=(string + "ingly")
    print(c)


