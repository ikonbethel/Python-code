#number printer less than input
#ikon beth

number = int(input("Enter number:"))
#number -= 1
count = 0

while number > 0:
    print(number)
    number -= 1
    if number == 0:
        print ("blast!"),("\a")

input("Exit:")
