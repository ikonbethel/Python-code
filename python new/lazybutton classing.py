#this is the lazy button creation using class
#demonstrates the use of tkinter with class
#created by ikon beth

from tkinter import *

class Application(Frame):
    """A GUI application with three buttons."""

    def __init__(self, master):
        """Initializing the Frame."""
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        """Create three buttons that do nothing."""
        #creating new button
        self.bttn1 = Button(self, text = "I do nothing!")
        self.bttn1.grid()

        #create second button
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text = "Me too!")

        #create the third buttn
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "Same here!"


#main

root =Tk()
root.title("Lazy Buttons")
root.geometry("200x85")

app = Application(root)
root.mainloop()
        
