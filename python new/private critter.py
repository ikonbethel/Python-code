#private critter program
#demonstrates private variables and methods
#as created by ikon beth


class Critter(object):
    """A virtual pet."""

    def __init__(self, name, mood):
        print("A new critter has been born!")
        self.name = name #public attribute
        self.__mood = mood   #private attribute

    def talk(self):
        print("\nI'm",self.name)
        print ("Right now, I feel", self.__mood, "\n")

    def __private_method(self):
        print("This is a private method.")

    def public_method(self):
        print("THis ia s public method.")
        self.__private_method()

crit = Critter(name = "Poochie", mood = "happy")
print (crit.talk)
#print(crit._Critter__mood)    #works but respect private attributes
#print (crit._Critter__private_method())    #works but respect private methods
crit.public_method()
input("Press enter key to exit:")
        
        


        
