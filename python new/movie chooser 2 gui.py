#this ia the movie chooser 2
#this demonstrates the use of radio button
#created by ikon beth


from tkinter import *

class Application(Frame):
    """Creates GUI Application for favorite movies."""

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        """Create widgets for the movie chooser program."""
        #create a label for tghe widget
        Label(self,
              text = "Choose your favorite movie."
              ).grid(row = 0, column = 0, sticky = W)

        #create an appluication widget
        Label(self, text = "Select one that applies"
              ).grid(row = 1, column = 0, sticky = W)

        self.favorite = StringVar()
        
        #create a radio button for comedy
        Radiobutton(self,
                    text = "Comedy",
                    value = "comedy",
                    variable = self.favorite,
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)

        #create a radio button for drama

        #self.favorite = StringVar()
        Radiobutton(self,
                    text = "Drama",
                    value = "comedy",
                    variable = self.favorite,
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W)

        #create a radio button for romance
        #self.favorite = StringVar()
        Radiobutton(self,
                    text = "Romance",
                    value = "comedy",
                    variable = self.favorite,
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W)


        #create a text widget to display the choice
        self.result_text = Text(self, width = 40, height = 5, wrap = WORD)
        self.result_text.grid(row = 5, column = 0, columnspan = 3)

    def update_text(self):
        """Updates text according to rthe choice made."""

        message = "Your favorite movie is "
        message += self.favorite.get()

        self.result_text.delete(0.0, END)
        self.result_text.insert(0.0, message)
#main
root = Tk()
root.title("Movie Chooser 2")
root.geometry("200x200")

app = Application(root)

root.mainloop()

        
        
        
        
        
