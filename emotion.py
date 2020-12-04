"""
This script is designed to obtain users' emotion of the moment.
It uses tkinter as a sketchy demonstration of user interface.
Users are able to select multiple emotions.
"""
from tkinter import *

class interface(object):
    def __init__(self, window):
        self.window = window
        # self.entry = Entry(self.window)

        self.window.title("Selecting your emotion")
        self.window.geometry("700x500")

        self.yscrollbar = Scrollbar(self.window)
        self.yscrollbar.pack(side = RIGHT, fill = Y)

        self.listbox = Listbox(window, selectmode = MULTIPLE, yscrollcommand = self.yscrollbar.set)
        self.listbox.pack(padx = 10, pady = 10, expand = YES, fill = "both")

        self.emotions = ["Happy", "Sad", "Satisfying", "Anger",
                         "Peaceful", "Fear", "Excitement", "Depressed",
                         "Contentment", "Sorrowful"]

        for emotion in range(len(self.emotions)):
            self.listbox.insert(END, self.emotions[emotion])
            # coloring alternative rows
            # orange: postive emotion
            # blue: negative emotion
            self.listbox.itemconfig(emotion, bg = "orange2" if emotion % 2 == 0 else "RoyalBlue1")

        self.label = None
        self.button = None
        self.items = None
        self.selection = self.listbox.curselection()

        self.display_selections()
        self.action()
        self.get_selection()

    def display_selections(self):

        self.label = Label(self.window,
                      text = "Hey! Choose one or more words that best describe your emotion of the moment (up to 3):  ",
                      font = ("Lucida Grande", 12),
                      padx = 10, pady = 10)
        self.label.pack()

        self.button = Button(self.window, text="Start!", command = self.action)
        self.button.pack()

    def get_selection(self):
        self.items = [self.emotions[int(item)] for item in self.listbox.curselection()]

    def action(self, event = None):
        self.output = Label(self.window)
        self.output.pack()
        self.output.config(text = 'We are getting your personalized movie list ...  ')

if __name__ == "__main__":
    window = Tk()
    interface = interface(window)
    window.mainloop()
    print(interface.selection)


