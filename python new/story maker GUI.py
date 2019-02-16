#mad lib program 2 using as many widgets as possible
#this creates stories based on the users input
#created by ikon beth


from tkinter import *

class Application(Frame):
    """Creates a GUI Application based on users input."""

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        """Creates widgets for user interactions."""

        #create an instruction label
        Label(self,
              text = "Enter information to create a story."
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        #create a label and entry text for the name of the person
        Label(self,
              text = "Person: "
              ).grid(row = 1, column = 0, sticky = W)

        self.person_entry = Entry(self)
        self.person_entry.grid(row = 1, column = 1, sticky = W)

        #create a label for plural nouns
        Label(self,
              text = "Plural Noun: "
              ).grid(row = 2, column = 0, sticky = W)
        
        self.noun_entry = Entry(self)
        self.noun_entry.grid(row = 2, column = 1, sticky = W)

        #create a label and text entry for a verb
        Label(self,
              text = "Verb:"
              ).grid(row = 3, column = 0, sticky = W)

        self.verb_entry = Entry(self)
        self.verb_entry.grid(row = 3, column = 1, sticky = W)

        #create a label for adjective entry
        Label(self,
              text = "Adjective(s)"
              ).grid(row = 4, column = 0, sticky = W)

        #an checkbutton for itchy
        self.its_itchy = BooleanVar()
        Checkbutton(self,
                    text = "Itchy",
                    variable = self.its_itchy
                    ).grid(row = 4, column = 1, sticky = W)
        
        #create a joyous checkbutton
        self.its_joyous = BooleanVar()
        Checkbutton(self,
                    text = "Joyous",
                    variable = self.its_itchy
                    ).grid(row = 4, column = 2, sticky = W)

        #create electric checkbutton
        self.its_electric = BooleanVar()
        Checkbutton(self,
                    text ="Electric",
                    variable = self.its_electric
                    ).grid(row = 4, column = 3, sticky = W)

        #create a label for body part radio button
        Label(self,
              text = "Body part(s)"
              ).grid(row = 5, column = 0, sticky = W)

        #create variable for single body part
        self.body_parts = StringVar()

        body_parts = ["bellybutton", "big toe", "medulla oblongata"]

        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_parts,
                        value = part
                        ).grid(row = 5, column = column, sticky = W)

            column += 1

        #create a submit button
        Button(self,
               text = "Click for story",
               command = self.tell_story
               ).grid(row = 6, column = 0, sticky = W)

        self.story_text = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_text.grid(row = 7, column = 0, columnspan = 4)


    def tell_story(self):
        """Fill in the story based on the user input."""

        #get values grom GUI
        person = self.person_entry.get()
        noun = self.noun_entry.get()
        verb = self.verb_entry.get()
        adjective = ""
        
        if self.its_itchy.get():
            adjective += "itchy, "
        if self.its_joyous.get():
            adjective += "joyous "
        if self.its_electric.get():
            adjective += "electric, "

        body_part = self.body_parts.get()
        
        #create a story

        story = "The famous explorer "
        story += person
        story += " had nearly given up a life-long quest to find The Lost City of "
        story += noun.title()
        story += " when one day, the "
        story += noun
        story += " found "
        story += person +". "
        story += "A strong, "
        story += adjective
        story += " perculiar feeling overwhelmed the explorer. "
        story += "After all this time, the quest was finally over. A tear came to "
        story += person +". "
        story += body_part + ". "
        story += "And then, the "
        story += noun
        story += " promptly devoured "
        story += person +". "
        story += "The moral of the story? Be careful what you "
        story += verb
        story += " for."

        #display the story
        self.story_text.delete(0.0, END)
        self.story_text.insert(0.0, story)

#main
root = Tk()
root.geometry("1000x1000")
root.title("Story maker")

app = Application(root)

root.mainloop()
        
            
                    

        
              
        
