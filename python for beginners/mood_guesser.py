#guess my mood program
#made by ikon beth
#on my path to mastering Python


import random
print("Do you know that I can measure your mood from your energy? Let's get started then!")
mood = int(random.randrange(4))
if mood ==int(("0")):
    print ("You are:" + " Happy!")
elif mood == int(("1")):
    print("You are:"+ " neutral!")
elif mood == int(("2")):
    print ("You are really:"+ " sad!")
else:
    print("Are you kidding me! Your mood swings like a gyroscope!")

input("Press the enter key to exit:")
