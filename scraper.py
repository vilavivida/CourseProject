"""
this script designed to scrape off information from two major movie rating websites: IMDB and Rotten Tomatoes
twelve movie ratings are obtained from each sources.
"""
from bs4 import BeautifulSoup as SOUP
import re
import requests

def locate_url(user_emotion):

    file_path = "url/"
    emotions = ["Happy", "Sad", "Satisfying", "Angry",
                "Peaceful", "Fearful", "Excited", "Depressed",
                "Content", "Sorrowful"]

    url_lst = []
    with open(file_path + "IMDB.txt") as f1, open(file_path + "RT.txt") as f2:
        f1_lst = f1.read().splitlines()
        f2_lst = f2.read().splitlines()
        for i in range(len(emotions)):
            if emotions[i] in user_emotion:
                IMDB = f1_lst[i]
                RT = f2_lst[i]
                url_lst.append(IMDB)
                url_lst.append(RT)

    return url_lst

"""sort movies based on their rating, from high to low
   through this function, the recommender is able to select the movie with highest rating and represent to users
"""
def rank_movies(movie_dict):
    ranked_dict = {}
    rating = []
    for movie_info in movie_dict.values():
        if type(movie_info[-1]) == float:
            rating.append(movie_info[-1])
    rating = sorted(rating, reverse = True)
    for r in rating:
        for k in movie_dict.keys():
            if movie_dict[k][-1] == r:
                ranked_dict[k] = movie_dict[k]
    return ranked_dict 
        
# IMDB should be a single link
def scrape_IMDB(IMDB, num): 
    response = requests.get(IMDB)
    data = SOUP(response.text, 'lxml')

    # we hope to have movie's name, grading, runtime, and rating
    IMDB_dict = {}
    title_lst = []

    # IMDB lists top 50 from each genre

    for movie in data.findAll('div', class_= "lister-item-content"):
        # title
        title = movie.find("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}) 
        title = str(title).split('">')[1].split('</')[0]
        IMDB_dict[title] = []
        title_lst.append(title)
        # grading
        grading = movie.find('span', class_= "certificate")
        if grading != None:
            grading = str(grading).split('">')[1].split('</')[0]
        else:
            grading = "N/A"
        IMDB_dict[title].append(grading)
        # runtime
        length = movie.find('span', class_ = "runtime")
        if length != None:
            length = str(length).split('">')[1].split('</')[0]
        else:
            length = "N/A"
        IMDB_dict[title].append(length)

    # rating
    for title, movie in zip(title_lst, data.findAll('div', class_ = "ratings-bar")):
        rating = movie.find('div', class_ = "inline-block ratings-imdb-rating")
        try :
            rating = float(re.search(r'[\d]*[.][\d]+', str(rating).split(' ')[3]).group())
        except AttributeError:
            rating = float(re.search(r'\d+', str(rating).split(' ')[3]).group())
        IMDB_dict[title].append(rating)

    ranked_dict = rank_movies(IMDB_dict)
    ranked_dict = dict(list(ranked_dict.items())[0: num])

    return ranked_dict

# RT should be a single link
def scrape_rt(RT, num):
    response = requests.get(RT)
    data = SOUP(response.text, 'lxml')
    RT_dict = {}
    title_lst = []
    rel_lst = []

    # Rotten Tomatoes lists top 100 from each genre

    # as above, we hope to obtain name, grading, runtime, and rating
    for movie in data.findAll('tr'):
        # title
        title = movie.find("a", class_ = "unstyled articleLink")
        if title != None:
            # link to movie profile
            rel_link = str(title).split('href="')[1].split('">\n')[0]
            rel_lst.append(rel_link)

            title = str(title).split('">')[1].split(" (")[0].strip('\n').strip()
            RT_dict[title] = []
            title_lst.append(title) #100

        ## (Do not run) numbers of reviews:
        # num_reviews = movie.find('td', class_ = "right hidden-xs")
        # if num_reviews != None:
        #     num_reviews = int(str(num_reviews).split('">')[1].split('</')[0]) #100
        #     RT_dict[title].append(num_reviews)

    # grading and runtime information are inside movie profile links
    for title, rel_link in zip(title_lst, rel_lst[:12]): #only 12 movies needed
        link = "https://www.rottentomatoes.com/" + rel_link
        response = requests.get(link)
        data_1 = SOUP(response.text, 'lxml')
        for div_tag in data_1.findAll('li', {'class':'meta-row clearfix'}):
            movie_label= div_tag.find('div', {'class': 'meta-label subtle'}).text
            if movie_label == "Rating:":
                rating_info = div_tag.find('div', {'class': 'meta-value'}).text
                rating_info = rating_info.replace("\n","").replace(" ", "")
                RT_dict[title].append(rating_info)
            elif movie_label == "Runtime:":
                runtime_info = div_tag.find('div', {'class': 'meta-value'}).text
                runtime_info = runtime_info.replace("\n","").replace(" ", "")

                RT_dict[title].append(runtime_info)
    # rating
    for title, movie in zip(title_lst, data.findAll('span', class_ = 'tMeterIcon tiny')):
        rating = movie.find('span', class_ = "tMeterScore")
        rating = str(rating).split('">\xa0')[1].split('%</')[0]
        #transform RT rating into the same scale as IMDB rating (out of 10)
        rating = int(rating)/10
        RT_dict[title].append(rating)

    ranked_dict = rank_movies(RT_dict)
    ranked_dict = dict(list(ranked_dict.items())[0: num])

    return ranked_dict

    