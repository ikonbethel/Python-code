#this is a movie chooser program
# demonstrates the use of check buttons
#created by ikon beth

from tkinter import *

class Application(Frame):
    """GUI Application for favourite movie types."""

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Creates widgets for movie type choice."""

        #create description label
        Label(self,
              text = "Choose your favourite movie types"
              ).grid(row = 0, column = 0, sticky = W)

        #create instruction label
        Label(self,
              text = "Select all that apply:"
              ).grid(row = 1, column = 0, sticky = W)

        

        #create comedy check button
        self.likes_comedy = BooleanVar()
        Checkbutton(self,
                    text = "Comedy",
                    variable = self.likes_comedy,
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)

        
       #create drama check button
        self.likes_drama = BooleanVar()
        Checkbutton(self,
                    text = "Drama",
                    variable = self.likes_drama,
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W)

        #create romance check button
        self.likes_romance = BooleanVar()
        Checkbutton(self,
                    text = "Romance",
                    variable = self.likes_romance,
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W)


        #create text field to display result
        self.result_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.result_txt.grid(row = 5, column = 0, columnspan = 3)


        


    def update_text(self):
        """Update text area and display user's favorite movie type."""
        likes = ("")

        if self.likes_comedy.get():
            likes += "You like comedic movies.\n"

        if self.likes_drama.get():
            likes += "You like dramatic movies.\n"

        if self.likes_romance.get():
            likes += "You like romantic movies.\n"

        self.result_txt.delete(0.0, END)
        self.result_txt.insert(0.0, likes)
        



#main
root = Tk()
root.title("Movie Chooser")

root.geometry("300x300")
app = Application(root)

root.mainloop()
        
        
        
