<img src="https://lionbridge.ai/wp-content/uploads/2020/09/2020-09-17_movie-recommendation-system.jpg" width="300" align="right" />

# MovieMood
## CS 410 Final Project: A Mood-Based Movie Recommendation System

### Project Overview

This is a Python-based movie recommendation system that implemented text-retrieval techniques and Graphical User Interface. One special thing about this system is that its recommendations were tailored around users' emotion of the moment. There are so many existing movie recommender systems available in the market, but only a small number of them were designed based on users' psychological needs. The main objective of this project is to fill this gap by making traditional recommender system more user-driven. <br>

### Emotion associated with Genre of Movie

There are **10** categories of emotion the system presented to users to choose from. These are **5** postive emotions *("Happy", "Satisfied", "Peaceful", "Excited", "Content")* and **5** negative emotions *("Sad", "Angry", "Fearful", "Depressed", "Sorrowful")*. These emotions taken as inputs from the GUI interface we built through tkinter (please refer to `interface.py`): 

<a href='https://postimg.cc/ns710phP' target='_blank'><img src='https://i.postimg.cc/s2H0f2ds/Screen-Shot-2020-12-09-at-3-27-42-PM.png' width="640" height="480" border='0' alt='Screen-Shot-2020-12-09-at-3-27-42-PM'/></a>

**The correspondence of every emotion with genre of movies are set up as below: <br/>**
 - Happy - Horror <br/>
 - Sad - Drama <br/>
 - Satisfied - Animation <br/>
 - Angry - Romance <br/>
 - Peaceful - Fantasy <br/>
 - Fearful - Adventure <br/>
 - Excited - Crime <br/>
 - Depressed - Comedy <br/>
 - Content - Mystery <br/>
 - Sorrowful - Action <br/>
 
Based on the inputted emotion, the system is going to be selected from the corresponding genre based on their ratings given by two websites: **IMDB** and **Rotten Tomatoes**. The reason why we are collecting movie information from both websites is that we believe the system is able to capture a more full-scaled opinions from movie lovers. 

### Application of Crawling

Because we intend to scrape two websites with different web structure, we developed one IMDB crawler and another RT crawler to extract movie information. Check out `scraper.py` for more details.<br/>
Here are two example movie pages of *IMDB* and *Rotten Tomatoes*: <br/>

<p float="left">
  <a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/XqhmY7TT/Screen-Shot-2020-12-09-at-4-43-36-PM.png' width="450" height="250" border='0' alt='Screen-Shot-2020-12-09-at-4-43-36-PM'/></a>
  <a href='https://postimg.cc/D461Jzyt' target='_blank'><img src='https://i.postimg.cc/Z0tHQBkK/Screen-Shot-2020-12-09-at-4-46-59-PM.png' width="450" height="250"  border='0' alt='Screen-Shot-2020-12-09-at-4-46-59-PM'/></a> 
</p>

As you can see, comparing to IMDB, Rotten Tomatoes includes the majority of movie information in each movie profile link. Our crawler had to look up each link to capture hidden information, such as *movie length, maturity grading, cast, etc*. Therefore, it is unavoidable that the program takes more time to scrape RT pages.

### Ranking and Scoring

We would pull user rating scores from both IMDb and Rotten Tomatoes. Due to the different rating scales used by IMDb and Rotten Tomatoes, we would first convert both scores to a *10-point scale* for the ease of comparison. We would also take the number of ratings into consideration, as larger number of ratings tends to make the overall rating more credible. Therefore, we would run *logistic regression* function on the number of ratings, and add it as an additional weightage to the final movie score.

### Present Movie Information

After users indicate their moods, the program is going to look up the corresponding link to the movie page and present movie information as `Treeview`, which is a module included by the tkinter library displaying a hierarchical collection of items.<br/>
Here is an example output of the list of recommended movies: <br/>

<a href='https://postimg.cc/DW34Jb9M' target='_blank'><img src='https://i.postimg.cc/W4hGyGXT/Screen-Shot-2020-12-13-at-4-16-31-PM.png' width="600" height="400" border='0' alt='Screen-Shot-2020-12-13-at-4-16-31-PM'/></a>

**Note: Not every movie has all information listed. If the crawler cannot find relevant information, it will automatically fill the space with "Not Found".**

### You May Also Like...

After users chose their favorite movie from the list, we would run a [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity) analysis to recommend **3** similar movies based on the summary.

Here is an example of movies similar to *Toy Story 4*: <br/>
<a href='https://postimg.cc/zbXBKw00' target='_blank'><img src='https://i.postimg.cc/85L68tWQ/Screen-Shot-2020-12-13-at-4-19-55-PM.png' width="600" height="400" border='0' alt='Screen-Shot-2020-12-13-at-4-19-55-PM'/></a>

### Self-evaluation
The work is equally distributed between the two teammates, and we were able to complete our mood-based movie recommender system as intended. We chose not to build a seperate mobile application, but instead spend the time working on additional features like cosine similarity and logistic regression. In the end, we have obtained the expected outcome. 

### Environment Set-up
Please check out `requirements.txt` for information.<br/>
You can install all packages at once using `$ pip install -r requirements.txt`. <br/>
*Please use **Python 3**. Otherwise you will need to import tkinter.ttk separately because it is not a submodule of tkinter in Python2*

### How to use?
After making sure you have all packages installed, activate the program through `main.py`. <br/>
The program will start running immediately.<br/>
*The scraping process may take up to **30 seconds**. Please do not close the tkinter window when the program is running.*

### Video Presentation
[YouTube link](https://youtu.be/DIIRPvu-ts0)
