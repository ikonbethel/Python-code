#Attribute Critter
#demonstrates creating and accessing object attributes
#ennoleht

class Critter(object):
    """A virtual pet."""
    def __init__(self, name):
        print("A new critter has been born!")
        self.name = name
        

    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        return rep

    def talk(self):
        print("Hi. I'm", self.name,"\n")


#main
crit1 = Critter("Rudolph")
crit1.talk()

crit2 = Critter("Randolph")
crit2.talk()

print ("Printing crit1:")
print(crit1)

print("Directly accessing crit1.name:")
print(crit1.name)

input("Press enter key to exit")
