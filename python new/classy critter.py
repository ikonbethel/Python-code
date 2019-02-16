#classy critter program
#demonstrates  lass attributes and static methods
#enno leht

class Critter(object):
    """A virtual pet."""
    total = 0

    def status():
        print("\nThere total number of critters is", Critter.total)

    status = staticmethod(status)

    def __init__(self, name):
        print ("A critter has been born!")
        self.name = name
        Critter.total += 1

#main
print("Accessing the class attribute Critter.total:"),
print(Critter.total)

print("\nCreating critters.")
crit1 = Critter("critter1")
crit2 = Critter("critter2")
crit3 = Critter("critter3")

Critter.status

print("\nAccessing the class attribute through an object:"),
print(crit1.total)

input("\nPress enter key to exit:")


    
