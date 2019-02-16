#this is a sample guess my number game using GUI
#DevCUyo100DaysOfCode
#created by ikon beth

from tkinter import *
import random
number = random.randrange(101)

class Application(Frame):
    """GUI Application for guessing a number."""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #create a description label
        Label(self,
              text = "This is a guess my number game"
              ).grid(row = 0, column = 0, columnspan = 3, sticky = W)

        #create a label and number entry for the number input
        Label(self,
              text = "Enter your number guess",
              ).grid(row = 1, column = 0, sticky = W)
        self.number_entry = Entry(self)
        self.number_entry.grid(row = 1, column = 1, sticky = W)



        #create a submit button
        Button(self,
               text = "Submit guess",
               command = self.answer_display
               ).grid(row = 2, column = 0, sticky = W)

        #create a textbox to display the result
        
        self.story_text = Text(self, width = 70, height = 5, wrap = WORD)
        self.story_text.grid(row = 5, column = 0, columnspan = 4)


    def answer_display(self):
        """Create the action for the number guess."""
        
        while int(self.number_entry.get())!= int(number):
            if int(self.number_entry.get()) < number:
                story = "The guess is lower! Try a higher number!"
            elif int(self.number_entry.get()) > number:
                story = "The guess is higher! Try a lower number!"
            break
        else:
            story = "You guessed right!The number is", number


        self.story_text.delete(0.0, END)
        self.story_text.insert(0.0, story)
            
                
        
        
        
        






root = Tk()
root.geometry("1000x1000")
root.title("Number Guesser")

app = Application(root)

root.mainloop()
