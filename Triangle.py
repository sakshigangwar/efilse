x=int(input("enter the number"))
y=int(input("enter the number"))
z=int(input("enter the number"))
num=x+y+z
if num==180:
    print("this triangle is vaild")
else:
    print("this is not triangle")




a=int(input("enter the side:"))
b=int(input("enter the side:"))
c=int(input("enter the side:"))
if a==b==c:
    print("equliteral triangle")
elif a==b or b==c or c==a:
    print("isoceles triangle")
elif a!=b!=c:
    print("scalene triangle")





a=int(input("enter the side"))
b=int(input("enter the side"))
c=int(input("enter the side"))
if a==b==c:
    print("equliteral")
else :
    print("not equal")