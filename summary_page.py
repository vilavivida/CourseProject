from tkinter import *
from tkinter.ttk import *

class Summary_Page(object):
	def __init__(self, window, targetMovies, targetMovieSummary, mainSummary):
		self.window = window
		self.window.title('Summary Page')
		self.window.geometry("700x500")
		
		self.mainSummary = mainSummary
		self.targetMovies = targetMovies
		self.targetMovieSummary = targetMovieSummary

		#add label
		self.label = Label(self.window, text = "Summary of the movie you selected")
		self.label.config(font =("Courier", 14))  
		self.label.pack()

		# show summary of the movie on tkinter window
		text = Text(self.window, height = 12, width = 70, bg = "light yellow")
		text.insert(INSERT, self.mainSummary)
		text.pack()

		#add label
		self.label_2 = Label(self.window, text = "Based on your search, here we recommend you to check out following movies:")
		self.label_2.config(font =("Courier", 14))  
		self.label_2.pack()

		# add similar movie options

		recText = Text(self.window, height = 30,  width = 70, bg = "light cyan") 
		for movie, summary in zip(self.targetMovies, self.targetMovieSummary):
			recText.insert(INSERT, "\n🎬" + movie + ": ")
			recText.insert(END, summary)
			recText.pack(expand=1, fill=BOTH)


# window = Tk()
# Summary_Page(window, targetMovies, targetMovieSummary, mainSummary)
# window.mainloop()

