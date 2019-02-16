#this illustrates a read it program
#how to read from an external file
#created by ikon

print("Opening and closing the file.")
text_file = open("read_it.txt", "r")
text_file.close()

print("\nReading character from the file.")
text_file = open("read_it.txt", "r")
print (text_file.read(1))
print (text_file.read(5))
text_file.close()

print("\nRead the entire text file at once.")
text_file = open("read_it.txt", "r")
whole_thing = text_file.read()
print (whole_thing)
text_file.close()


print("\nReading character from the line.")
text_file = open("read_it.txt", "r")
print (text_file.readline(1))
print (text_file.readline(5))
text_file.close()

print("\nReading one line at a time.")
text_file = open("read_it.txt", "r")
print (text_file.readline())
print (text_file.readline())
print (text_file.readline())
text_file.close()


print("\nRead the entire text file into a list.")
text_file = open("read_it.txt", "r")
lines = text_file.readlines()
print (lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()

print("\nLooping through the file,line by line")
text_file = open("read_it.txt", "r")
for line in lines:
    print(line)
text_file.close()

input("\nPress enter key to exit")

