#this is a sample write to file program
#created bty ikonbeth

print("Creating a text file with the write()method.")
text_file = open("write_itt.txt", "w")

text_file.write("This is line 1\n")
text_file.write("This becomes line 2\n")
text_file.write("This makes this to be line 3\n")
text_file.close()

