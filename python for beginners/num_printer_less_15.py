#this demonstrates how to break an infinite loop
#created by ikon
#getting there!
print("This prints number up to 15 from your input and no more")
number = int(input("Type in your number: "))
while number <= int(("15")):
    number += int("1")
    print("your number is: ",number)
    if number == int(("15")):
        break
print ("You have exceeded the maximum answer!")
input("Press enter key to exit:")
