#name and meaning dictionary of ikonne family illustrating dictionary
#created by Ikon beth
Family_Igbo_Name = {"Chibuzo":"God has first priority",
                    "Chigozie":"God bless",
                    "Chibueze":"God is the King",
                    "Chibundu":"God is life",
                    "Chibuike":"God is strength",
                    "Chioma":"Good God",
                    "Amarachi":"Grace of God",
                    "Ozioma":"Good news",
                    "Chijioke":"God has the share",
                    "Chidera":"Once God has written",
                    "Toochukwu":"Praise God",
                    "Ikechukwu":"God's strength",
                    "Chinaememma":"God that shows goodness",
                    "Chiemela":"God has done it",
                    "Amaechi":"Who knows tommorrow",
                    "Chinedu":"God leads",
                    "Ogadimma":"It will be well",
                    "Uchendu":"The will of life",
                    "Chinyere":"God gave it",
                    "Onyinye":"Gift",
                    "Uzoamaka":"The way is good",
                    "Chiamaka":"God is beautiful"}
print \
    ("""
    Family Igbo Name Definition Interactive
    0 - Exit
    1 - Look up a name's meaning
    2 - Add a new name and meaning
    3 - Redefine or modify a name's meaning
    4 - Delete a name and meaning
    """)
choice = input("Choice: ")
if choice == ("0"):
    print("Good-Bye")

elif choice ==("1"):
    name = input("\nType in the name of interest: ")
    name = name.title()
    if name in Family_Igbo_Name:
        print(Family_Igbo_Name.get(name))

elif choice ==("2"):
    entry = input("\nType in the name: ")
    entry = entry.title()
    if entry not in Family_Igbo_Name:
        meaning = input("\nType in the English meaning of the name: ")
        Family_Igbo_Name[entry] = meaning
        print("\nThe name" ,entry," has been added to the dictionary")
    else:
        print ("\nThe name", entry, "is already in the list")
elif choice == ("3"):
    entry = input("\nWhat name do you want to modify: ")
    entry = entry.title()
    if entry in Family_Igbo_Name:
        meaning = input("\nWhat is the English meaning of the name?: ")
        Family_Igbo_Name[entry] = meaning
        print("\nThe name", entry, "has been modified")
    else:
        print("\nThe name", entry, "does not exist. Try adding it to the list")
elif choice ==("4"):
    entry = input("\nWhat name do you want to remove:")
    entry = entry.title()
    if entry in Family_Igbo_Name:
        del Family_Igbo_Name[entry]
        print("\nThe name", entry, "has been deleted")
    else:
        print("\nThe name", entry, "is either not yet born or is dead")

input("\nPress enter key to exit")
    
    
    
    
    
    

