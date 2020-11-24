"""
this script designed to scrape off information from two major movie rating websites: IMDB and Rotten Tomatoes
twelve movie ratings are obtained from each sources.
"""
from bs4 import BeautifulSoup as SOUP
import re
import requests

def locate_url(user_emotion):
    file_path = "url/"
    emotions = ["Happy", "Sad", "Satisfying", "Anger",
                "Peaceful", "Fear", "Excitement", "Depressed",
                "Contentment", "Sorrowful"]

    with open(file_path + "IMDB.txt") as f1, open(file_path + "RT.txt") as f2:
        f1_lst = f1.read().splitlines()
        f2_lst = f2.read().splitlines()
        for i in range(len(emotions)):
            if user_emotion == emotions[i]:
                IMDB = f1_lst[i]
                RT = f2_lst[i]
                url_lst = [IMDB, RT]

    return url_lst

def scrape_IMDB(url_lst):
    IMDB = url_lst[0]
    response = requests.get(IMDB)
    data = SOUP(response.text, 'lxml')

    # we hope to have movie's name, grading, runtime, and rating
    # TODO: adding number of reviews
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
            grading = "Grading information is not found"
        IMDB_dict[title].append(grading)
        # runtime
        length = movie.find('span', class_ = "runtime")
        if length != None:
            length = str(length).split('">')[1].split('</')[0]
        else:
            length = "Film's length is not found"
        IMDB_dict[title].append(length)

    # rating
    for title, movie in zip(title_lst, data.findAll('div', class_ = "ratings-bar")):
        rating = movie.find('div', class_ = "inline-block ratings-imdb-rating")
        try :
            rating = float(re.search(r'[\d]*[.][\d]+', str(rating).split(' ')[3]).group())
        except AttributeError:
            rating = float(re.search(r'\d+', str(rating).split(' ')[3]).group())
        IMDB_dict[title].append(rating)

    # we need a maximum of twelve movies from each genre >> website based on the algorithm
    IMDB_dict = dict(list(IMDB_dict.items())[0: 12])

    return IMDB_dict

def scrape_rt(url_lst):
    RT = url_lst[1]
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

        # reviews
        num_reviews = movie.find('td', class_ = "right hidden-xs")
        if num_reviews != None:
            num_reviews = int(str(num_reviews).split('">')[1].split('</')[0]) #100
            RT_dict[title].append(num_reviews)

    # TODO: figuring out a way to reduce the time it takes for going through movie profile links

    # movie_info_lst = []

    # grading and runtime information are inside movie profile link
    # for rel_link in rel_lst[:12]: #only 12 movies needed
    #     link = "https://www.rottentomatoes.com/" + rel_link
    #     response = requests.get(link)
    #     data = SOUP(response.text, 'lxml')
    #     for div_tag in data.findAll('li', {'class':'meta-row clearfix'}):
    #         movie_info = div_tag.find('div', {'class': 'meta-value'}).text
    #         movie_info = movie_info.replace(" ", "").strip('\n').strip('\t')
    #         movie_info_lst.append(movie_info)

    # rating
    for title, movie in zip(title_lst, data.findAll('span', class_ = 'tMeterIcon tiny')):
        rating = movie.find('span', class_ = "tMeterScore")
        rating = str(rating).split('">\xa0')[1].split('%</')[0]
        #transform RT rating into the same scale as IMDB rating (out of 10)
        rating = int(rating)/10
        RT_dict[title].append(rating)

    RT_dict = dict(list(RT_dict.items())[0: 12])

    return RT_dict

url_lst = locate_url("Happy")
print(scrape_rt(url_lst))





    