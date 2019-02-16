#this program simulates an ATM machine program
#created by Ikon beth
#DevCUyo100DaysOfcode
#day005
proceed = ("yes")
#proceed1 = ("ok")
#deny = ("no")
trial = int("0")
#trial = int(trial)
trial1 = int("0")
#trial1 = int(trial1)
balance = int("100000")
amount =("0")
#amount = int(amount)
#check = (amount%1000)
#check = int(check)
account = ("")
bank = ("")
phone = ("")
password1 =("")
print(\
    """
    \tWELCOME TO THE BETHBANK
    THE BEST BANK IN THE SUBSAHARAN AREA OF AFRICA
    \tYOUR SATISFACTION IS OUR NUMBER ONE PRIORITY


    SLOT IN YOUR CARD TO ACCESS OUR SERVICES
    TYPE IN YES IF CARD IS IN MACHINE OR NO IF NOT IN MACHINE
    """)
answer = input("\nSlot in your card to continue!: ")
answer = answer.lower()
while answer != (proceed):
    answer = input("\nSlot in your card to continue!: ")
    trial += "1"
    if trial >= "3":
        input("Press enter key to exit")

else:
    password1 = input("\nType in your password to proceed: ")
    print(\
    """
    \t\tWELCOME TO OUR SERVICE PANEL
    CHOOSE FROM OUR VARIED RANGE OF SERVICES
    (1)- WITHDRAWAL          (2) - CHECK BALANCE
    (3) - TRANSFER LOCALLY    (4) - INTERNATIONAL TRANSFER
    (5) - RECHARGE YOUR PHONE
    """)
    choice = int(input("\nChoose from your preferred service:"))
    
    if choice == int("1"):
        password = input("\nConfirm your password to proceed:")
        while password != (password1):
            password = input("\nConfirm your password to proceed:")
            trial += int("1")
            if trial == int("3"):
                print ("\nTake back your card! Access Denied! Thank you!")
                break
                
        else:
            amount = int(input("\nType in your withdrawal amount: "))
            while (amount%1000) != int("0"):
                print("\nYou can only withdraw multiples of 1000")
                amount = int(input("\nType in your withdrawal amount: "))
                trial += int("1")
                if trial >=int("3"):
                    print ("\nTake back your card! Access Denied! Thank you!")
                    break
                
            else:
                while amount >=(balance):
                    print("\nInsufficient fund. You have, "+"$",balance, "Try a lower amount")
                    amount = int(input("\nType in your withdrawal amount: "))
                        
                else:
                    balance -= amount
                    print("\nWithdrawal Successful! You current balance is $",balance)
                    print ("\nTake back your card and continue with any other transaction")
                    

    elif choice == int(("2")):
        password = input("\nConfirm your password to proceed:")
        while password != (password1):
            password = input("\nConfirm your password to proceed:")
            trial += 1
            if trial >= 3:
                print ("\nTake back your card! Access Denied! Thank you!")
                break
        else:
            print ("Your current balance is $",balance)
            print ("\nTake back your card and continue with any other transaction")
           

    elif choice == int(("3")):
        password = input("\nConfirm your password to proceed:")
        while password != (password1):
            password = input("\nConfirm your password to proceed:")
            trial += int("1")
            if trial >= int("3"):
                print ("\nTake back your card! Access Denied! Thank you!")
                break
        else:
            account = input("\nType in the destination account number: ")
            bank = input("Type in the destination bank: ")
            amount = int(input("\nType in your transfer amount: "))
            while amount >=(balance):
                print("\nInsufficient fund. You have, "+"$",balance,"."+ "Try a lower amount")
                amount = int(input("\nType in your transfer amount: "))
                trial += int("1")
                if trial >= int(("3")):
                    print ("\nTake back your card! Access Denied! Thank you!")
                    break
            else:
                balance = balance - amount
                print("\nTransfer Successful! You current balance is $",balance)
                print ("\nTake back your card and continue with any other transaction")
            
    elif choice ==int(("4")):
        password = input("\nConfirm your password to proceed:")
        while password != (password1):
            password = input("\nConfirm your password to proceed:")
            trial += int("1")
            if trial >= int("3"):
                print ("\nTake back your card! Access Denied! Thank you!")
                break
        else:
            account = input("\nType in the destination account number: ")
            bank = input("Type in the destination bank: ")
            amount = int(input("\nType in your transfer amount: "))
            while amount >=(balance):
                print("\nInsufficient fund. You have, "+"$",balance,"."+ "Try a lower amount")
                amount = int(input("\nType in your transfer amount: "))
                trial += int("1")
                if trial >= int(("3")):
                    print ("\nTake back your card! Access Denied! Thank you!")
                    break
            else:
                balance = balance - amount
                print("\nTransfer Successful! You current balance is $",balance)
                print ("\nTake back your card and continue with any other transaction")
            

    elif choice == int("5"):
        password = input("\nConfirm your password to proceed:")
        while password != (password1):
            password = input("\nConfirm your password to proceed:")
            trial += int("1")
            if trial >= int("3"):
                print ("\nTake back your card! Access Denied! Thank you!")
                break
        else:
            phone = int(input("\nType in the number you want to recharge:"))
            amount = int(input("\nType in your recharge amount: "))
            while amount >= int(balance):
                print("\nInsufficient fund. You have, "+"$",balance,"."+ "Try a lower amount")
                amount = int(input("\nType in your recharge amount: "))
                trial += int("1")
                if trial >= int(("3")):
                    print ("\nTake back your card! Access Denied! Thank you!")
                    break
            else:
                balance -= amount
                print("\nRecharge Successful! You current balance is $",balance)
                print ("\nTake back your card and continue with any other transaction")
           
    else:
        while choice > int("5"):
            choice = int(input("\nChoose from your preferred service: "))
            trial += int("1")
            if trial >= int(("3")):
                print ("\nTake back your card! Access Denied! Thank you!")
                break


print("\nThank you for your patronage! We hope you had a wonderful service?")
print("We are always here for you!")
input("\nPress enter key to exit:")
            
        
                    
                    
    
            
            
    
    
    
    
