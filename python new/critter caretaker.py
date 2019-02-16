#Critter caretaker
#A virtual pet to care for
#created by ikon beth

class Critter(object):
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def __get_mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            mood = "happy"
        elif 5<= unhappiness <= 10:
            mood = "okay"
        elif 11 <= unhappiness <=15:
            mood = "frustrated"
        else:
            mood = "mad"
    mood = property(__get_mood)

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now\n")
        self.__pass_time()

    def eat(self, food = 4):
        print("Brrrrp. Thank you!")
        self.hunger -= food
        if self.hunger <= 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Wheeee")
        self.boredom -= fun
        if self.boredom <= 0:
            self.boredom = 0
        self.__pass_time()

def main():
        crit_name = input("What do you want to name your kitten?:")
        crit = Critter(crit_name)

        choice = None
        while choice != "0":
            print(\
            """Critter Caretaker
            0 - Quit
            1- Listen to your critter
            2 - Feed your critter
            3 - Play with your critter
            """)
            choice = int(input("Choice:"))

            if choice ==int("0"):
                print("Good bye!")

            elif choice == int("1"):
                crit.talk()
                
            elif choice == int("2"):
                crit.eat()

            elif choice ==int("3"):
                crit.play()

            else:
                print("\nSorry, but", choice, "is not valid.")
                break


main()
input("Press enter key to exit:")

            
                
            
        
        
        
