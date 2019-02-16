#this prints a multiplication table based on the user's input
#designed by ikon beth

num = 0

number = int(input("Type in your number to print it's multiplication table:"))
for i in range (1, 13):
    num += 1
    print (num ," x ", number, "=", num*number)

input("\nExit:")
    
