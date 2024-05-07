from textblob import TextBlob
import numpy as np

def classify_sentiment(polarity, thresholds=(-0.05, 0.05)):
    """Classify sentiment based on polarity and dynamic thresholds."""
    if polarity < thresholds[0]:
        return "Negative"
    elif polarity > thresholds[1]:
        return "Positive"
    else:
        return "Neutral"

def analyze_reviews(reviews):
    """Analyze a list of reviews and return sentiments."""
    polarities = [TextBlob(review).sentiment.polarity for review in reviews]
    # Dynamically determine thresholds based on polarity distribution
    lower_threshold = np.percentile(polarities, 25)  # 25th percentile
    upper_threshold = np.percentile(polarities, 75)  # 75th percentile
    
    sentiments = [classify_sentiment(polarity, (lower_threshold, upper_threshold)) for polarity in polarities]
    return sentiments

# Example reviews
reviews = [
    "The movie was an incredible journey, I loved every moment!",
    "It was a decent movie, not too bad but could be better.",
    "I really disliked the movie. It was boring and too long.",
    "The plot was interesting, but the execution could have been better.",
    "Absolutely a masterpiece, stunning visuals and gripping plot!"
]

# Analyzing reviews
sentiments = analyze_reviews(reviews)
for review, sentiment in zip(reviews, sentiments):
    print(f"Review: {review}\nSentiment: {sentiment}\n")
