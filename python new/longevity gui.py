#longevity program gui from tkinter
#demonstrates the text and entry widgets, and the grid layout manager
#created by ikon beth


from tkinter import *

class Application(Frame):
    """GUI Application whih can reveal the secret of longevity."""

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        """Creates button, text and entry widgets."""
        #create instruction label
        self.inst_lbl = Label(self, text = "Enter password for secret of longevity")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        #create entry widget to accept password
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)

        #create submit button
        self.submit_bttn = Button(self, text = "Submit", command = self.reveal)
        self.submit_bttn.grid(row = 2, column = 0, sticky = W)

        #create a text widget to display message
        self.secret_txt = Text(self, width  = 35, height =5, wrap = WORD)
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def reveal(self):
        """Displays message based on the password."""
        contents = self.pw_ent.get()

        if contents == "secret":
            message = "Here's the secret of living up to 100: Live to 99 "\
                      "and then be VERY careful."

        else:
            message = "That's not the correct password, so I cannot share "\
                      "the secret with you."

        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)


#main
root = Tk()
root.title("Longevity")
root.geometry("250x150")

app = Application(root)

root.mainloop()

        
        
        
        
