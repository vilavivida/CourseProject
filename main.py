import interface
from scraper import locate_url, rank_movies, scrape_IMDB, scrape_rt
import movie_page

from tkinter import *

if __name__ == "__main__":

    # call interface.py

    window = Tk()
    interface = interface.interface(window)
    window.mainloop()
    user_inputs = [] # obtain user selections
    for i in interface.result:
        user_inputs.append(interface.emotions[i])

    # apply self-built crawler

    user_emotion = user_inputs
    url_lst = locate_url(user_emotion)
    movie_dict = {}
    for url in url_lst:
        if "www.imdb.com" in url:
            if len(user_emotion) == 1:
                movie_dict.update(scrape_IMDB(url, 12))
            elif len(user_emotion) == 2:
                movie_dict.update(scrape_IMDB(url, 6))
            elif len(user_emotion) == 3:
                movie_dict.update(scrape_IMDB(url, 4))
        elif "www.rottentomatoes.com" in url:
            if len(user_emotion) == 1:
                movie_dict.update(scrape_rt(url, 12))
            elif len(user_emotion) == 2:
                movie_dict.update(scrape_rt(url, 6))
            elif len(user_emotion) == 3:
                movie_dict.update(scrape_rt(url, 4))
    movie_dict = rank_movies(movie_dict)
    
    # load movie page
    root = Tk()
    movie_page = movie_page.movie_page(root, movie_dict)
    root.mainloop()









