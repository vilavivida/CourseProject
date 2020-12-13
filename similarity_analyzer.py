import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

stopwords = stopwords.words('english')

# Cleaning and preprocessing the summary 
def preprocess(text):
    # remove punctuation
    text = ''.join([w for w in text if w not in string.punctuation])
    # remove case
    text = text.lower()
    # remove stopwords
    text = ' '.join([w for w in text.split() if w not in stopwords])
    return text

# Find the 3 most similar movie summaries
def find3MostSim(movie_dict, summary_list):

    # stores each movie's summary
    summary = summary_list[0]

    # the last string in summary is our target for summary similarity analysis
    summary.append(summary_list[1])

    processed = list(map(preprocess, summary))

    # create matrix of unique words
    vectorizer = CountVectorizer().fit_transform(processed)
    vectors = vectorizer.toarray()

    # run cosine similarity analysis
    similarity = cosine_similarity(vectors)

    # find the 3 most similar movies by their summary
    target = similarity[-1]
    target[-1] = 0
    targetIndex = sorted(range(len(target)), key=lambda x: target[x])[-3:]

    return targetIndex


