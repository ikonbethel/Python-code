#this prints a deck of card and reshufles it
#created by ikon beth

from random import shuffle
import random
card = ("Heart ", "Spade ", "Club ","Diamond ")
numlist = ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,'J','K','Q','A')
m =[]
t = []
for i in card:
    for j in numlist:
        m += [i+str(j)]
shuffle(m)
print(m)
input("Exit:")
        
    
