#this is a click counter gui
#demonstrating the binding of an event with an event handler
#created by ikon beth

from tkinter import *

class Application(Frame):
    """GUI  application which counts button click."""

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widgets()

    def create_widgets(self):
        """Create button which displays number of clicks."""
        self.bttn = Button(self)
        self.bttn["text"] = "Total Clicks: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    

    def update_count(self):
        """Increase clik amount and display new total."""
        self.bttn_clicks += 1
        self.bttn["text"] = "Total Clicks:" +str(self.bttn_clicks)

#main


root = Tk()
root.title("Click Counter")
root.geometry("200x50")
app = Application(root)
root.mainloop()
