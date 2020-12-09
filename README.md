<img src="https://lionbridge.ai/wp-content/uploads/2020/09/2020-09-17_movie-recommendation-system.jpg" width="300" align="right" />

# Mood-Based Movie Recommendation System
## CS 410: Final Project 

### Overview
> This is a collaborative work done by [Vivian Yu](https://github.com/vilavivida) and [Chenyu Zhao](https://github.com/chenyuzhao98). 

> This is a Python-based movie recommendation system that implemented text-retrieval techniques and Graphical User Interface. One special thing about this system is that its recommendations were tailored around users' emotion of the moment. There are so many existing movie recommender systems available on the market, but only a small number of them were designed based on users' psychological needs. The main objective of this project is to fill this gap by making traditional recommender system more user-driven. <br>

### Emotion associated with Genre of Movie

There are **10** categories of emotion the system presented to users to choose from. These are **5** postive emotions *("Happy", "Satisfying", "Peaceful", "Excited", "Content")* and **5** negative emotions *("Sad", "Angry", "Fearful", "Depressed", "Sorrowful)*. Here, these are taken as inputs from the GUI interface we built through tkinter: 

<a href='https://postimg.cc/ns710phP' target='_blank'><img src='https://i.postimg.cc/s2H0f2ds/Screen-Shot-2020-12-09-at-3-27-42-PM.png' width="640" height="480" border='0' alt='Screen-Shot-2020-12-09-at-3-27-42-PM'/></a>

**The correspondence of every emotion with genre of movies are set up as below: <br/>**
 - Happy - Horror <br/>
 - Sad - Drama <br/>
 - Satisfying - Animation <br/>
 - Angry - Romance <br/>
 - Peaceful - Fantasy <br/>
 - Fearful - Adventure <br/>
 - Excited - Crime <br/>
 - Depressed - Comedy <br/>
 - Content - Mystery <br/>
 - Sorrowful - Action <br/>
 
Based on the input emotion, the system is going to be selected from the corresponding genre based on their ratings given by two websites: **IMDB and Rotten Tomatoes**. The reason why we are collecting movie information from both websites is that we believe the system is able to capture a more full-scaled opinions from movie lovers. 

