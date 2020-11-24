"""
This script is designed to obtain users' emotion of the moment.
It uses tkinter as a sketchy demonstration of user interface.
Users are able to select multiple emotions.
"""

from tkinter import * 

class interface(object):
    def __init__(self, window):
        self.window = window
        self.window.geometry("500x200")

        self.yscrollbar = Scrollbar(self.window) 
        self.yscrollbar.pack(side = RIGHT, fill = Y) 

        self.listbox = Listbox(window, selectmode = MULTIPLE, yscrollcommand = self.yscrollbar.set)
        self.listbox.pack(padx = 10, pady = 10, expand = YES, fill = "both")
        self.listbox.bind("<Double-1>", self.call)

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
        self.selection = self.listbox.curselection()

    def Display_Selections(self):

        self.window = Tk()
        self.window.title("Selecting your emotion")

        self.label = Label(self.window, 
                      text = "Hey! Choose one or more words that best describe your emotion at the moment:  ", 
                      font = ("Lucida Grande", 12),  
                      padx = 10, pady = 10) 
        self.label.pack()

    def call(self, a):
        if len(self.listbox.curselection()) > 3:
            for i in self.listbox.curselection():
                if i not in self.selection:
                    self.listbox.selection_clear(i)
        self.selection = self.listbox.curselection()

window = Tk()
interface(window)
window.mainloop()


