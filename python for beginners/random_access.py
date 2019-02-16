#random access program
#by ikon

import random
word = ("index")
print ("The word is: ",word)

high = len(word)
low = -len(word)
position = random.randrange(low, high)
for i in range(10):
    print("word[", position, "]\t", word[position])

input("\nPress enter key to exit")
           
