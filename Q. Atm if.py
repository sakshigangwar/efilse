print("WEL COME SBI BANK")
atm=input("enter your card:")
if atm=="credit card" or atm=="debit card":
    print("after")
    language=input("please select your lenguage")
    if language=="english" or language=="hindi":
        print("next")
        account=input("select your account")
        if account=="saving account"or account=="current account":
            print("continue with the saving account")
            code=int(input("enter the code number 1 to 10"))
            if code>=4:
                print("wait for checking password")
                amount=int(input("enter the amount"))
                if amount>500 or amount<=100000:
                    print("plz wait your tranzaction id in prosses")
                    recipt=input("want recipt")
                    if recipt=="yes" or recipt=="no":
                        print("transition successfully")
                        print("thankyou")
                    else:
                        print("plz collect your recip")
                else:
                    print(" enter amount is not avilable")
            else:
                print("plz check your pin code")
        else:
            print("plz check your account")
    else:
        print("check language")
else:
    print("something wrong")


        