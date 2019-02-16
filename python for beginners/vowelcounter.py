#vowel counter
#by ikon beth

vowels = "aeiou"
goo = vowels.split()
count = 0
print ("This program counts the vowels in your sentence(s)")
letter = input("Type in your sentence:")

if vowels in letter.lower():
    count += 1
    
print("There are ", count, "vowels in your sentence")
input("Exit")
