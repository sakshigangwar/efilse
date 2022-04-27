totalmarks=int(input("enter the marks"))
sutdentmarks=int(input("enter the marks"))
percentege=(sutdentmarks/totalmarks*100)
if percentege>=90:
    print("A grade")
elif percentege>=80:
    print("B grade")
elif percentege>=70:
    print("C grade")
elif percentege>=60:
    print("D grade")
elif percentege>=40:
    print("E grade")
elif percentege<40:
    print("F grade")
else:
    print("fail")