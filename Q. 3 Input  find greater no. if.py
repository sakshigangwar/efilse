a=int (input("enter the number::"))
b=int (input("enter the number::"))
c=int (input("enter the number::"))
if a>b and a>c:
    print (a,"is greater")
elif b>c and b>a:
    print (b,"is greater")
elif c>b and c>a:
    print (c,"is greater")
else: 
    print ("lesser ")