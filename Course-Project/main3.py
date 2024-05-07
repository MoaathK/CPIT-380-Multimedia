from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


nltk.download('vader_lexicon')

def aspect_based_sentiment_analysis(review, aspects):
    blob = TextBlob(review)
    aspect_sentiments = {}
    
    for sentence in blob.sentences:
        for aspect, keywords in aspects.items():
            if any(keyword in sentence.lower() for keyword in keywords):
                sentiment = sentence.sentiment.polarity
                if aspect not in aspect_sentiments:
                    aspect_sentiments[aspect] = []
                aspect_sentiments[aspect].append(sentiment)
    
    # Calculate average sentiment for each aspect found
    aspect_summary = {aspect: sum(sentiments) / len(sentiments) if sentiments else 0
                      for aspect, sentiments in aspect_sentiments.items()}
    return aspect_summary

# Example usage:
aspects = {
    "acting": ["acting", "performance", "cast"],
    "visuals": ["visuals", "cinematography", "effects"],
    "plot": ["plot", "storyline", "narrative"]
}



def classify_sentiment(polarity):
    """Classify the sentiment based on polarity."""
    if polarity > 0.05:
        return "Positive"
    elif polarity < -0.05:
        return "Negative"
    else:
        return "Neutral"
    


def printAllTheInfo(detailed_sentiments):
    writeFile  = open(r"./Course-Project/review-analysis-output.txt","wt")
    #filename = "./review-analysis-output.txt"
    for sentiment in detailed_sentiments:
        writeFile.write(f"\nReview: {sentiment['review']}"
            f"\nPolarity: {sentiment['polarity']},
            \nSubjectivity: {sentiment['subjectivity']},
            "f"\nIntensity: {sentiment['intensity']},
            "f"\nSentiment Classification: {sentiment['classification']},
            \nKey Words: {', '.join(sentiment['key_words'])}\n")
    return writeFile

def analyze_sentiment_details(reviews):
    sia = SentimentIntensityAnalyzer()
    vectorizer = TfidfVectorizer(stop_words='english')

    # Calculate TF-IDF scores to identify significant words
    tfidf_matrix = vectorizer.fit_transform(reviews)
    feature_names = vectorizer.get_feature_names_out()

    detailed_reviews = []
    
    for review, tfidf_vec in zip(reviews, tfidf_matrix):
        blob = TextBlob(review)
        vader_scores = sia.polarity_scores(review)
        tfidf_scores = np.array(tfidf_vec.todense()).flatten()

        # Find top 3 significant words based on TF-IDF scores
        top_indices = np.argsort(tfidf_scores)[-2:]
        topWord = []
        for index in top_indices:
            if tfidf_scores[index] >0:
                word = feature_names[index]
                topWord.append(word)
        

        detailed_reviews.append({
            'review': review,
            'polarity': round(blob.sentiment.polarity,4),
            'subjectivity': round(blob.sentiment.subjectivity,4),
            'intensity': round(vader_scores['compound'],3),
            'classification': classify_sentiment(blob.sentiment.polarity),
            'key_words': topWord
        })
        
    return detailed_reviews

# Example reviews
reviews = [
    "The movie was an incredible journey, I loved every moment!",
    "It was a decent movie, not too bad but could be better.",
    "I really disliked the movie. It was boring and too long.",
    "The plot was interesting, but the execution could have been better.",
    "Absolutely a masterpiece, stunning visuals and gripping plot!"
]
letterBoxedReviews = ["got the 4D experience by forgetting to drink water today and watching this extremely dehydrated",
                      "not bad if u ever just feel like staring at the color orange and not feeling a single emotion for two and a half hours",
                      "favourite movie.",
                      "155 minutes of industrial design and thousand-yard-stares while Hans Zimmer honks at you with his giant mechanical goose."]


# Analyze reviews
def main():
    detailed_sentiments = analyze_sentiment_details(letterBoxedReviews)
    fileOutput = printAllTheInfo(detailed_sentiments)
    review = "The acting was superb, but the plot was somewhat lacking. The visuals were stunning."
    aspect_sentiments = aspect_based_sentiment_analysis(review, aspects)
    print(aspect_sentiments)


main()
