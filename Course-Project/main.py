from textblob import TextBlob

# Example review
review = "The movie was fantastic! The visuals were stunning and the storyline was captivating."

# Create a TextBlob object
blob = TextBlob(review)

# Get the sentiment of the text
sentiment = blob.sentiment

print(f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")

# Determining sentiment category
if sentiment.polarity > 0.2:
    print("Positive sentiment")
elif sentiment.polarity < -0.2:
    print("Negative sentiment")
else:
    print("Neutral sentiment")
