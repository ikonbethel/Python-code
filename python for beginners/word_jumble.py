#word jumble game training
#computer picks a random word and jumbles it
#the player has to guess the right word
#by ikon beth

import random
#create a seequence of words to choose from
WORDS = ("python", "jumper", "lucky", "difference", "phone", "stand")
#pick one word randomly from WORDS
word = random.choice(WORDS)
#assign it to correct to see if its correct.lol
correct = word
#creating a jumbled version of the word
jumbled =""

while word:
    position = random.randrange(len(word))
    #creating a new version of jumbled word
    jumbled += word[position]
    #creating a new version of word
    word = word[:position] + word[(position + 1): ]

#welcoming the player to the game
name = input("Type in your name: ")
print(("\t\tWelcome to the Word Jumble Game!,")+name)
print("\tUnscramble the letters to make a word!")
print(("\nThe jumbled word is: ")+jumbled)
guess = input("\nYour guess: ")
guess = guess.lower()
while (guess !=correct and guess !=("")):
    print("Sorry, that's not it!")
    guess = input("\nYour guess: ")
    guess = guess.lower()
if (guess ==correct):
    print("\n\nThat's it! You guessed right!")
    print(("\n\nThanks for playing, ")+ name)
    

input("Press enter to exit")

    
    

