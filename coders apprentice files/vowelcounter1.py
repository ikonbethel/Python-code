#
#

message = input("Enter your message: ")
new_message = ""
VOWELS = ("aeiou")

for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        #print("A new message has been created: ",new_message)
#print("\nYour new message without vowels is: ",new_message)
print("There are ", len(message) - len(new_message), " vowels in your sentence")
input("Press enter key to exit:")
