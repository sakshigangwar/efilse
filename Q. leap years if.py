# year=int(input("enter the year"))
# if year%400==0 or year%4==0 and year!=100:
#     print ("this is a leap year,a")
# else:
#     print ("this is a not leap year")



year=int(input("enter the year:"))
if year%4==0:
    if year%400==0:
        print("century")
    else:
        print("it is a leapyear")
else:
    print("error")




