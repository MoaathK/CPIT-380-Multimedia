from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Ensure necessary NLTK datasets are downloaded
nltk.download('vader_lexicon')

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
        top_indices = np.argsort(tfidf_scores)[-3:]
        top_words = [feature_names[index] for index in top_indices if tfidf_scores[index] > 0]

        detailed_reviews.append({
            'review': review,
            'polarity': blob.sentiment.polarity,
            'subjectivity': blob.sentiment.subjectivity,
            'intensity': vader_scores['compound'],
            'key_words': top_words
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

# Analyze reviews
detailed_sentiments = analyze_sentiment_details(reviews)
for sentiment in detailed_sentiments:
    print(f"Review: {sentiment['review']}\n"
          f"Polarity: {sentiment['polarity']}, Subjectivity: {sentiment['subjectivity']}, "
          f"Intensity: {sentiment['intensity']}\nKey Words: {', '.join(sentiment['key_words'])}\n")
