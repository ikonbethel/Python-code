#this simulates a label in gui
#created by ikon beth

from tkinter import *

#creating a root window
root = Tk()
root.title("Lazy Buttons")
root.geometry("200x85")

#create a frame to hold other widgets
app = Frame(root)
app.grid()


#creating button in the frame
bttnl = Button(app, text = "I do nothing")
bttnl.grid()

#create the seond button
bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text ="me too!")


#creating the third button
bttn3 = Button(app)
bttn3.grid()
bttn2["text"] = "Same here"

#kick off the window's event loop
root.mainloop()
