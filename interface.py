"""
This script is designed to obtain users' emotion of the moment.
It uses tkinter as a sketchy demonstration of user interface.
Users are able to select multiple emotions.
"""

from tkinter import *

class interface(object):
    def __init__(self, window):
        self.window = window
        self.window.title("Select your emotion")
        self.window.geometry("700x500")

        self.yscrollbar = Scrollbar(self.window) 
        self.yscrollbar.pack(side = RIGHT, fill = Y) 

        # set up label
        self.label = Label(self.window, 
              text = "Hey! Choose one or more words that best describe your emotion of the moment (up to 3)\n (Please do not close this window)",
              font = ("Lucida Grande", 12),
              padx = 10, pady = 10)
        self.label.pack()

        # set up listbox
        self.listbox = Listbox(window, selectmode = MULTIPLE, yscrollcommand = self.yscrollbar.set)
        self.listbox.pack(padx = 10, pady = 10, expand = YES, fill = "both")

        self.emotions = ["Happy", "Sad", "Satisfying", "Angry",
                         "Peaceful", "Fearful", "Excited", "Depressed",
                         "Content", "Sorrowful"]

        for emotion in range(len(self.emotions)):
            self.listbox.insert("end", self.emotions[emotion])
            # coloring alternative rows
            # orange represents postive emotions
            # blue represents negative emotions
            self.listbox.itemconfig(emotion, bg = "orange2" if emotion % 2 == 0 else "RoyalBlue1")
        self.listbox.select_set(0)
        self.listbox.focus_set()

        self.result = None
        self.window.bind("<Return>", self.exit_gui)

        # add user-friendly label
        T = Text(self.window, height = 2, width = 30)
        T.pack()
        T.insert(END, "Press <Return> when you are \nfinished with your selection")

    def exit_gui(self, event):
        global result
        self.result = list(self.listbox.curselection())
        self.window.destroy()

if __name__ == "__main__":
    window = Tk()
    interface = interface(window)
    window.mainloop()
    user_inputs = [] # obtain user selections
    for i in interface.result:
        user_inputs.append(interface.emotions[i])