#this computes a factorial of a number
#created by ikon beth


print("\t\tThis prints a factorial of a given number")

num = int(input("Enter the number:"))
number  = num + 1
get = 1

while number >= 0:
    number -= 1
    get *= number
    if number == 1:
        print ("The factorial of ", num, " is ", get)
          
