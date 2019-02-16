#creating a second tuple  demonstration
#this is part of hero's inventory
#created by ikon beth

#create tuple with elements
inventory = ("shield", "armor", "healing potion", "magic", "sword")
for item in inventory:
    print("\nYou have got this wonderful toy in your inventory!:"),print (item)

input("\nPress enter key to continue: ")
#to get the number of items one has
print ("\nYou have ",len(inventory)," items in your possession")
input("\nPress enter key to continue: ")
#test for membership in item
#if "healing potion" in inventory:
#    print ("You will live to fight another day")
#display one item through an index
index = int(input("\nEnter the index number of an item you got in inventory to see it's importance: "))
print("\nAn index", index, "is", inventory[index])
#while True:
#   index = int(input("\nEnter the index number of an item you got in inventory to see it's importance: "))
#   if index ==(""):
#       continue
if index ==int(0):
    print("You cannot be reached by sword easily and your first layer of defence is intact")
elif index ==int(1):
    print ("Your second layer of protection is intact! You will survive long.")
elif index ==int(2):
    print ("You have many lives! Your third layer of protection is intact!")
elif index ==int(3):
    print("Your are the mmost dangerous warrior alive! Ride on to victory!")
elif index ==int(4):
    print("Attack and destroy the enemies!")
input("\nPress enter key to exit:")


