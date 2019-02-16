#this simulates a label in gui
#created by ikon beth

from tkinter import *

#creating a root window
root = Tk()
root.title("Labeller")
root.geometry("200x50")

#create a frame to hold other widgets
app = Frame(root)
app.grid()

#create a label in the frame
lbl = Label(app, text = "I'm a label")
lbl.grid()

#kick off the window's event loop
root.mainloop()
