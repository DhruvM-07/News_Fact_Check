from textblob import TextBlob

def analyze_sentiment(text):
    """Performs Sentiment Analysis on the given text."""
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity  # Range: -1 (Negative) to +1 (Positive)

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"
