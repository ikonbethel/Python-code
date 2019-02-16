# A tipper code
# calculates your tip to a waiter in a restaurant
# written by ikonne
name = input("Welcome! What is your name?:")
ale = int(input("How many gallons of ale did you order?:"))
ale1 = int(ale*150)
beer = int(input("How many gallons of beer did you order?:"))
beer1 = int(beer*200)
nkwobi = int(input("How many plates of nkwobi did you order?:"))
nkwobi1 = int(nkwobi*750)
total = int(ale1) + int(beer1) + int(nkwobi1)
tip1 = 0.15*total
tip2 = 0.2*total
total1 = 1.15 * total
total2 = 1.2 * total
print("Hope you enjoyed your stay with us," + " " + name + "?" + " " + "Your bill is" + " " + "#" + str(total1)+ "(i.e.," + str(total)+ "+" + str(tip1)+ ")" + " " + "or if you are feeling generous," + " " + "#" + str(total2)+ "(i.e.," + str(total)+ "+" + str(tip2)+ ")")
print ("Have a nice and blessed day")
print ("See you next time!")
input("Press enter key to exit:")
