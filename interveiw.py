num=int(input("enter the class"))
if num>=1 and num<=9:
    aim=input("enter the aim")
    if aim>"a" or aim>"A" and aim<"z" or aim<"Z":
        print(aim)
if num==10:
    sub=input("enter the sub")
    if sub>"a" or sub>"A" and sub<"z" or sub<"Z":
        print(sub)
if num==11 or num==12:
    clg=input("enter the clg")
    if clg>"a" or clg>"A" and  clg<"z" or clg<"Z":
        print(clg)
        corse=input("enter the corse")
        if corse>"a" or corse>"A" and corse<"z" or corse<"Z":
            print(corse)