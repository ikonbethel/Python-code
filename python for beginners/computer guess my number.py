#can the computer predict my number/
#let me know how many guesses it takes the computer to correctly guess my number
#created by ikon beth

import random
number = int("66")
guess  = int("0")

computer = random.randrange(101)
while computer != number:
    if computer <= number:
        print("You got a lower number! Try again!")
        computer = random.randrange(101)
        guess += 1
    elif computer >= number:
        print ("You got a higher number! Try again!")
        computer = random.randrange(101)
        guess += 1
else:
    print("\nThe computer correctly guessed my number", computer, "in", guess, "guesses")
    
input("\nPress the enter key to exit")
