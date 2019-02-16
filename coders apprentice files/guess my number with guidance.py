# this program tries to guess my number
#respondes based on my guidance
#created by ikon beth

import random
guessed = 87
high = 100
low = 1
num = random.randint(low, high)
tries = 0


while num != 87:
    print("I, computer, guessed ",num)
    ans = input("Am I correct? If no, what do I do?(L/H/Y):")
    tries += 1
    if ans.lower() == "l":
        num = random.randint(low, num)

    elif ans.lower() == "h":
        num = random.randint(num, high)
else:
    print("Puny human!, I got your number, ",num," in ",tries," tries.")
        
    
