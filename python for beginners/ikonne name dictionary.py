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
                    "Uzoamaka":"The way is good"}

name = input("Type in the Igbo name of any of your family member: ")
name = name.title()
while name in Family_Igbo_Name:
    print(Family_Igbo_Name[name])
    break
input("Press enter key to exit: ")
