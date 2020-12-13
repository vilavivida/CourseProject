"""
scrape the summary of each chosen movie to facilitate users' selection.
to avoid the trouble of going through the entire collection of movie summaries,
we are only interested in summary of the movie if user clicked it
"""

from bs4 import BeautifulSoup as SOUP
import re
import requests

## (DO NOT RUN) For Testing Purpose:
from scraper import movie_dict
user_input = 'Get Out'

# we only need folder_path if we are going to download all summary info
def get_movie_summary(movie_dict, user_input):
    summary_list = []
    sub_list = []
    summary_list.append(sub_list)

    """
    In cosine-similarity measure, we are going to take main_summary as target and sub_summary as reference pool
    """

    # for IMDB
    # when the movie is clicked by the user
    for movie_title, movie_info in zip(movie_dict, movie_dict.values()):
        if movie_title == user_input:
            summary_list.append(movie_info[0])

    ## (optional) store movie summaries into collective folder
    ## print(main_summary, file = open("{}.txt".format(folder_path + title),"a"))

    # we are collecting other movie summaries to prepare for cosine-similarity calculation
        elif movie_title in movie_dict.keys():
            sub_list.append(movie_info[0])
                
    ## print(sub_summary, file = open("{}.txt".format(folder_path + title),"a"))

    return summary_list

summary_list = get_movie_summary(movie_dict, user_input)
# print(len(summary_list[0]))







