#randon number generator
#not to be used in online gaming programs cos it is highly predictable
#created by ikonne
import random
#generates random numbers 1-6
die1 = random.randrange(6) + 1
die2 = random.randrange(6) + 1
total = die1 + die2
print("You rolled a die which are" + " " + str(die1) + " " + "and" " " + str(die2) + " " + "which totals" + " " + str(total))
input ("Press enter key  to exit:")
