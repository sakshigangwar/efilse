print("visit google account creation page")
email=input("want to creat email")
if email=="yes":
    print("next")
    username=input("enter the name")
    if username>"A" and username<"Z" or username>"a" or username<"z":
        print("next")
        lastname=input("enter lastname")
        if lastname>"A" and lastname<"Z" or lastname>"a" and lastname<"z":
            print("next")
            number=int(input("enter the number"))
            if number<=1 or number>=1000000000:
                print("next")
                birthday=int(input("enter the date birth"))
                if birthday==birthday:
                    print("next")
                    gender=input("enter gender")
                    if gender=="female":
                        print("next")
                        email=input("enter your own email adderes")
                        if email and "@gmail.com"in email:
                            print("next")
                            password=input("enter the password")
                            if password>="letters" and "other symbols" and "number":
                                print("your email is created")
                            else:
                                print("your password wrong")
                        else:
                            print("invailed adderes")
                    else:
                        print("something wrong")
                else:
                    print("error")
            else:
                print("nothing")
        else:
            print("erroe")
    else:
        print("something wrong")
else:
    print("error")
