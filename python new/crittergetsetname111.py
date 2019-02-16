#property critter
#demonstrates the get and set methods and property
#created by ikon beth
#BP59G
class Critter(object):
    """A virtual pet."""

    def __init__(self, name):
        print("A new critter has been born!")
        self.__name = name
#using get method,
        
    def get_name(self):
        return self.__name
#using set method
    
    def set_name(self, new_name):
        if new_name == "":
            print("A critter's name cannot be empty!")
        else:
            self.__name = new_name
            print("Name successfully changed!")

    name = property(get_name, set_name)

    def talk(self):
        print("\nHi. I'm ", self.name)


#main

crit = Critter("Rudolph")
crit.talk()
print("\nMy critter name is:")
print(crit.name)
print("\nAttempting to change my critter's name.")
crit.name = ""
print("\nAttempting to change my critter's name again.")
crit.name = "Poochie"
crit.talk()
input("\nPress enter key to exit:")

 
