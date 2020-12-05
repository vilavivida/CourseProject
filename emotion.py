"""
This script is designed to obtain users' emotion of the moment.
It uses tkinter as a sketchy demonstration of user interface.
Users are able to select multiple emotions.
"""

from tkinter import *
from tkinter.ttk import *

class interface(object):
    def __init__(self, window):
        self.window = window
        self.window.title("Selecting your emotion")
        self.window.geometry("700x500")

        self.yscrollbar = Scrollbar(self.window)
        self.yscrollbar.pack(side = RIGHT, fill = Y)

        # set up label
        self.label = Label(self.window,
              text = "Hey! Choose one or more words that best describe your emotion of the moment (up to 3):  ",
              font = ("Lucida Grande", 12),
              padx = 10, pady = 10)
        self.label.pack()

        # set up listbox
        self.listbox = Listbox(window, selectmode = MULTIPLE, yscrollcommand = self.yscrollbar.set)
        self.listbox.pack(padx = 10, pady = 10, expand = YES, fill = "both")

        self.emotions = ["Happy", "Sad", "Satisfying", "Anger",
                         "Peaceful", "Fear", "Excitement", "Depressed",
                         "Contentment", "Sorrowful"]

        for emotion in range(len(self.emotions)):
            self.listbox.insert("end", self.emotions[emotion])
            # coloring alternative rows
            # orange: postive emotion
            # blue: negative emotion
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

# TODO: import movie_dict from scraper.py and add to the class
# TODO: migrate interface class

class movie_page(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.create_UI()
        self.load_table()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def create_UI(self):
        pg = Treeview(self)
        columns = ["Rating", "Runtime", "Grading"]
        pg['columns'] = ("Rating", "Runtime", "Grading")
        pg.heading("#0", text = "Titles", anchor = "w")
        pg.column("#0", anchor = "w")
        for column in columns:
            pg.heading('{}'.format(column), text = '{}'.format(column))
            pg.column('{}'.format(column), anchor = 'center', width = 100)
        pg.grid(sticky = (N,S,W,E))
        self.treeview = pg
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def load_table(self):
        self.treeview.insert('', 'end', text="call you by my name", values=('10.00',
                             '121 min', 'TV-14'))

if __name__ == "__main__":
    # interface
    # window = Tk()
    # interface = interface(window)
    # window.mainloop()
    # user_inputs = [] # obtain user selections
    # for i in interface.result:
    #     user_inputs.append(interface.emotions[i])

    # movie_page
    root = Tk()
    movie_page(root)
    root.mainloop()

