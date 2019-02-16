#property critter
#demonstrates the get and set methods and property
#created by ikon beth

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
        print("Hi. I'm ", self.name)

        
crit = Critter(object)
crit.set_name("Randolph")
#crit.set_name("")   still works
print (crit.name)
crit.name = "Sammy"


