from tkinter import *
from tkinter.ttk import *

class movie_page(Frame):
    def __init__(self, parent, movie_dict):
        Frame.__init__(self, parent)
        self.movie_dict = movie_dict
        self.columns = ["Movie Score", "Movie Length", "Maturity Rating"]
        self.create_UI()
        self.load_table()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def create_UI(self):
        pg = Treeview(self)
        pg['columns'] = tuple(self.columns)
        pg.heading("#0", text = "Titles", anchor = "w")
        pg.column("#0", anchor = "w")
        for column in self.columns:
            pg.heading('{}'.format(column), text = '{}'.format(column))
            pg.column('{}'.format(column), anchor = 'center', width = 100)

        pg.grid(sticky = (N,S,W,E))
        self.treeview = pg
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def load_table(self):
        for movie_title in self.movie_dict:
            movie_info = self.movie_dict[movie_title]
            # some movies do not have grading and runtime information
            if len(movie_info) == 2:
                movie_info.insert(0, "Not Found")
            elif len(movie_info) == 1:
                movie_info.insert(0, "Not Found")
                movie_info.insert(1, "Not Found")
            self.treeview.insert('', 'end', text="{}".format(movie_title),
                                values=('{}'.format(movie_info[2]),'{}'.format(movie_info[1]),
                                '{}'.format(movie_info[0])))



