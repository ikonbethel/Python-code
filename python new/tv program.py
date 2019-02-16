#this is a program to simulate a television
#here, user can enter a channel number, change volume within a range of 0~70 at steps of 5
#this uses class, methods, and objects
#created by ikon beth


#DevCUyo100DaysOfCode
#day 6

class Television(object):
    
    
    
    def switch_off(self):
        print ("Television is powering off! Thanks for your patronage.")

    def select_channel(self):
        #self.channel = channel
        try:
            no = int(input("Input your channel number:"))
        except(ValueError):
            print("Letters and symbols not inclusive!")
        while int("0") <= no >= int("151"):
            print("\nInvalid number selected. Try again.")
            try:
                no = int(input("Input your channel number:"))
            except(ValueError):
                print("Try again!")
        else:
            print("\nChannel number", no, "now streaming!")
            

    def change_vol(self):
        volume = int(35)
        print("Press 9 to increase volume or 3 to reduce your volume.")
        vol = int(input("Increase or decrease volume?:"))
        if vol == int("9"):
            amount = int(input("By how much do you wish to increase volume?:"))
            total = volume + amount
            if total <= 70:
                print("Volume is:",total)
            elif total > 70:
                volume = 70
                print("maximum volume!:"),
                print(volume)
                
                
        elif vol == int("3"):
            amount = int(input("By how much do you wish to decrease volume?:"))
            total1 = volume - amount
            if total1 <= 0:
                volume = 0
                print("Volume muted!"),
                print(volume)
            else:
                print("Volume is:", total1)                
def main():
    tv = Television()
    """ Welcome to Beth Telecommunication Network(BTN)."""

    choice = None
    while choice != 0:
        print("""\
              Beth Television Network(BTN)\
              Welcome to our Esteemed User! Kind choose from the panel what you\
              want to do.\

              Choice
              0 - Switch off your television
              1 - Select a channel
              2 - Change volume
              """)
        break
    try:
        choice = int(input("Choice:"))
    except(ValueError):
        print("GOOD - BYE!")

    if choice == 0:
        tv.switch_off()
        
    elif choice == 1:
        tv.select_channel()

    elif choice == 2:
        tv.change_vol()

    else:
        print ("Invalid selection!")

main()
input("\nPress enter key to exit:")
        
        
              
    
    
              
                  
              
              
              
              
        
        
              
              
              
                  
              
              
              
              
               
