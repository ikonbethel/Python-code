#Exclusive Network login
#demonstrates logical operators conditions
#ikonbeth coding
print ("\tExclusive Computer Network")
print("\t\tMembers Only Access!\n")

security = 0
username =("")
while not username:
    username = input("Username: ")

password =("")
while not password:
    password = input("Password: ")
    
if username ==("ikonbethel@gmail.com") and password ==("ikonbethel31"):
    print("Hello ! Welcome Mr. Ikonbethel")
    security  = ("5")

elif username ==("lehtebennoci@gmail.com") and password ==("lehtebennoci31"):
    print("Hi, Lehteb!. Welcome")
    security = ("4")

elif username ==("ikonbeth.ib@gmail.com") and password ==("ikonbeth.ib31"):
    print ("Hi, Ikon.ib, Welcome")
    security = ("3")

elif username  ==("ikonbeth@yahoo.com") and password ==("ikonbeth31"):
    print ("Ikonbeth!. Good to see you again")
    security = ("2")

elif username ==("guest") or password ==("guest"):
    print (" Welcome our Esteemed Guest!")
    security = ("1")

else:
    print("\tLogin failed! You are not an Exclusive member")

input("Press enter key to exit")
