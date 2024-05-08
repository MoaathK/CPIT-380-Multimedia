from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


nltk.download('vader_lexicon')

def classify_sentiment(polarity):
    if polarity > 0.05:
        return "This Movie review is Positive"
    elif polarity < -0.05:
        return "This Movie review is Negative"
    else:
        return "This Movie review is Neutral"
    


def printAllTheInfo(detailed_sentiments):
    writeFile  = open(r"./Course-Project/review-analysis-output.txt","wt")
    for sentiment in detailed_sentiments:
        writeFile.write(f"\nReview: {sentiment['review']}\n"
            f"Polarity: {sentiment['polarity']}\n"
            f"Subjectivity: {sentiment['subjectivity']}\n"
            f"Intensity: {sentiment['intensity']}\n"
            f"Sentiment Classification: {sentiment['classification']}\n"
            f"Key Words: {', '.join(sentiment['key_words'])}\n")
    return writeFile


# 
def MovieSentimentReview(reviews):
    sia = SentimentIntensityAnalyzer()
    vectorizer = TfidfVectorizer(stopWords='english')

    # Calculate TF-IDF scores to get the most importent words
    tfidfMatrix = vectorizer.fit_transform(reviews)
    featureNames = vectorizer.get_feature_names_out()

    detailed_reviews = []
    # this iterartion will go throghout all the reviews provided to Know if they are 'Positive', 'Negative', 'Neutral'
    for review, tfidfVec in zip(reviews, tfidfMatrix):
        blob = TextBlob(review)
        vaderScores = sia.polarity_scores(review)
        tfidfScores = np.array(tfidfVec.todense()).flatten()

        # Find top 2 significant words based on TF-IDF scores that we calculated 
        top_indices = np.argsort(tfidfScores)[-2:]
        topWord = []
        for index in top_indices:
            if tfidfScores[index] >0:
                word = featureNames[index]
                topWord.append(word)
        
        # we will append the reviews to a format way
        detailed_reviews.append({
            'The Review': review,
            'polarity Of the review': round(blob.sentiment.polarity,4),
            'subjectivity': round(blob.sentiment.subjectivity,4),
            'intensity': round(vaderScores['compound'],3),
            'Review classification': classify_sentiment(blob.sentiment.polarity),
            'Key words': topWord
        })
        
    return detailed_reviews

# *Delete This After Editing*  Example reviews, Muhanned choice the best method that you would like on providing The Reviews.
reviews = [
    "The movie was an incredible journey, I loved every moment!",
    "It was a decent movie, not too bad but could be better.",
    "I really disliked the movie. It was boring and too long.",
    "The plot was interesting, but the execution could have been better.",
    "Absolutely a masterpiece, stunning visuals and gripping plot!"
]
# here is the Review Example, We could choice more reviews Based on movies from LetterBoxed
letterBoxedReviews = ["got the 4D experience by forgetting to drink water today and watching this extremely dehydrated",
                      "not bad if u ever just feel like staring at the color orange and not feeling a single emotion for two and a half hours",
                      "favourite movie.",
                      "155 minutes of industrial design and thousand-yard-stares while Hans Zimmer honks at you with his giant mechanical goose."]


# Main function
def main():
    # calling the Movie Sentiment Review Function, and returing the reviews
    detailedSentiments = MovieSentimentReview(letterBoxedReviews)
    # here i wrote all the review sentiment in a file that you can read from it later
    fileOutput = printAllTheInfo(detailedSentiments)
    # you could play with this file as you like
main()
