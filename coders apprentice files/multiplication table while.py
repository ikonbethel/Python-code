#this print a multiplication table using a while loop
#created by ikon beth

number = int(input("Enter number to print it's times table:"))
x = 0

while x < 12:
    x += 1
    print ( x, " X ", number, "=", x*number)

input("\nExit:")
