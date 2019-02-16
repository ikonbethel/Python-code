#Simple critter tutorial
#demonstrates a basic class and object
#enno leht

class Critter(object):
    """A virtual pet."""
    def talk(self):
        print("Hi. I'm an instance of class Critter.")
    def cry(self):
        print("HMMMMMMMMMMMMMMMMM")
    def laugh(self):
        print ("HAHHHHAHAHAHAHAHAHA!")
        

#main

crit = Critter()
crit.talk()
crit.laugh()
input("Press enter key to exit:" )
