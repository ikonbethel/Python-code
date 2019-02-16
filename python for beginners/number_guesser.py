#guess my number game
#allows gamer to correctly guess my number between 1 and 100
#created by ikonbeth
import random

print("\t\tGUESS MY NUMBER!")
name = input("Type in your name,Gamer!: ")
print ("Welcome to guess my number",name)
print ("Guess my number between 1 and 100 and know how many guesses it takes you")

#setting of variables
no = int(random.randrange(101))
number = int(input("Start your guess: "))
tries = int("1")
while number != no:
    if number > no:
        print(" Guess lower...")
    else:
        print ("Guess higher...")

    number = int(input("Start your guess: "))
    tries += 1

else:
    print ("You guess is correct! The number is " , number)
    print (" You got it in ", tries , "tries")

input("Press enter key to exit")


