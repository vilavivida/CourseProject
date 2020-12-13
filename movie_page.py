from tkinter import *
from tkinter.ttk import *
import time


class Waiting_Page(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.title("we are collecting your movie data")
        self.geometry("700x500")
        # require to pop up a window before getting into mainloop
        self.ProgressBar()
        self.update()

    def ProgressBar(self):
        self.bar = Progressbar(self, orient="horizontal", length=300,
                               mode="indeterminate")
        self.bar.place(x=10, y=5, height=20, width=300)
        self.bar.start()


class movie_page(Frame):
    def __init__(self, parent, movie_dict):
        Frame.__init__(self, parent)

        # pop up the waiting page
        self.parent = parent
        self.parent.geometry("700x500")
        self.parent.title("Double click on the movie you are most interested in. 🙅‍♀️❎🙅‍♂️Close the window when you are done.")
        self.parent.withdraw()
        waiting = Waiting_Page(self)

        self.movie_dict = movie_dict
        self.columns = ["Movie Score", "Movie Length", "Maturity Rating"]
        self.create_UI()
        self.load_table()
        self.grid(sticky=(N, S, W, E))
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        time.sleep(2)
        waiting.destroy()
        self.parent.deiconify()  # show the window again
        self.selected_movie = [] # we are going to present summaries of selected movies


    def create_UI(self):
        pg = Treeview(self)
        pg['columns'] = tuple(self.columns)
        pg.heading("#0", text="Titles", anchor="w")
        pg.column("#0", anchor="w")
        for column in self.columns:
            pg.heading('{}'.format(column), text='{}'.format(column))
            pg.column('{}'.format(column), anchor='center', width=100)

        pg.grid(sticky=(N, S, W, E))
        self.treeview = pg
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.treeview.bind("<Double-1>", self.OnDoubleClick)
        # self.treeview.bind("<Return>", self.Quit)

    def load_table(self):
        for movie_title in self.movie_dict:
            movie_info = self.movie_dict[movie_title]

            # In case some movies do not have all information provided
            if len(movie_info) == 3:
                movie_info.insert(0, "Not Found")
            elif len(movie_info) == 2:
                movie_info.insert(0, "Not Found")
                movie_info.insert(1, "Not Found")
            elif len(movie_info) == 1:
                movie_info.insert(0, "Not Found")
                movie_info.insert(1, "Not Found")
                movie_info.insert(2, "Not Found")

            self.treeview.insert('', 'end', text="{}".format(movie_title),
                                 values=('{}'.format(movie_info[3]), '{}'.format(movie_info[2]),
                                         '{}'.format(movie_info[1])))
    def OnDoubleClick(self, event):
        self.item = self.treeview.identify('item', event.x, event.y)
        self.selected_movie.append(self.treeview.item(self.item, "text"))

    # def Quit(self, event):
    #     self.parent.destroy()



