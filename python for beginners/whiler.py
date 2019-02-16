#demonstrating while-loop using an multiple of 5 identifier
#created by ikon
#on my path of becoming a programmer
print("Do you want to know what your number represents?")
number= int(input("Type in your number:"))
x =int(number%5)
while x != int(("0")):
    number = int(input("Type in your number:"))
    x =int(number%5)
print("You got the multiple of 5!")
input("Press enter key to exit")
    
