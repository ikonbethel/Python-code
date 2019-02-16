#constructor critter
#demonstrates constructor
#enno leht


class Critter(object):
    """A critter has been born."""
    def _init_(self):
        print("A new critter has been born!")

    def talk(self):
        print("\nHi. I am a new instance of critter!")

    def laugh(self):
        print("HAHAHAHAHAHAHAHAHAHAHA")


#main
crit1 = Critter()
crit2 = Critter()
crit1.talk()
crit2.laugh()
input("Press enter key to exit:")
