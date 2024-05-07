from textblob import TextBlob
import numpy as np

def classify_sentiment(polarity, thresholds=(-0.05, 0.05)):
    

    if polarity < thresholds[0]:
        return "Negative"
    elif polarity > thresholds[1]:
        return "Positive"
    else:
        return "Neutral"

def analyze_reviews(reviews):
   
    polarities = [TextBlob(review).sentiment.polarity for review in reviews]
    # Dynamically determine thresholds based on polarity distribution
    lower_threshold = np.percentile(polarities, 25)  # 25th percentile
    upper_threshold = np.percentile(polarities, 75)  # 75th percentile
    
    sentiments = [classify_sentiment(polarity, (lower_threshold, upper_threshold)) for polarity in polarities]

    return sentiments

# Example reviews
reviews = [
    "The Godfather is a boring movie, and it shouldn't be in the top 10 movies.",
    "The movie was an incredible journey, I loved every moment!",
    "It was a decent movie, not too bad but could be better.",
    "I really disliked the movie. It was boring and too long.",
    "The plot was interesting, but the execution could have been better.",
    "Absolutely a masterpiece, stunning visuals and gripping plot!",
    "Azoz was the best actor in the whole film"
]
letterBoxedReviews = ["got the 4D experience by forgetting to drink water today and watching this extremely dehydrated",
                      "not bad if u ever just feel like staring at the color orange and not feeling a single emotion for two and a half hours",
                      "Anakin's favourite movie.",
                      "155 minutes of industrial design and thousand-yard-stares while Hans Zimmer honks at you with his giant mechanical goose."]

# Analyzing reviews
#for x in reviews:
 #   print(x)

sentiments = analyze_reviews(letterBoxedReviews)
for review, sentiment in zip(letterBoxedReviews, sentiments):
    print(f"Review: {review}\nSentiment: {sentiment}\n")
