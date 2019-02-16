#this finds the third side of the right angled triangle using Pythagoras theorem
#this is on function creation
#created by ikon

from math import *
import sys
a =int(input("Type in the first number:"))
b = int(input("Type in the second number:"))
def Pythagoras(a,b):
    #from math import sqrt
    if int(a) <0 or int(b) < 0:
        print("Error!")
        #exit()
    else:
        c = sqrt(a*a + b*b)
        print("The third Pythagorean triple is ", c)


Pythagoras(a,b)

input("Exit:")

    
