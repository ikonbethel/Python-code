#nested sequence of high score program using tuple and while synthax
#created by Ikon Beth
scores = []
choice = ""
while choice !="0":
    print( \
    """
    High Score Keeper
    0 - Quit
    1 - List scores
    2 - Add a score
    """)
    choice = input("Choice:")
    if choice ==("0"):
        print("Good_bye")
    elif choice ==("1"):
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name,"\t", score)
    elif choice ==("2"):
        name = input("What is the player's name?: ")
        score = input("What score did the player get?: ")
        entry = (score, name)
        scores.append(entry)
        scores.sort()
        scores.reverse()
        scores = scores[:5]
    
else:
        print("Sorry, but ",choice," is invalid!")
input("Press enter key to exit")
        
    
    
