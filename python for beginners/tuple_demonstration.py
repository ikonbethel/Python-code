#hero's inventory program
#this uses and demonstrates the use of tuples as contrast to lists
#created by ikon beth

#first create an empty tuple
inventory = ()
#treat the tuple as a condition
if not inventory:
    print("You are empty handed")

input("Peress enter key to continue")
#create a tuple with some items

inventory = ("shield",
             "armor",
             "shield",
             "healing potion")
print("\nThe tuple inventory is: ",inventory)
#print the items seperately
for item in inventory:
    print (item)
input ("Press enter key to exit")
