from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text.
    Returns:
        - Sentiment Score: (-1 to 1, where -1 is very negative, 1 is very positive)
        - Sentiment Label: Negative, Neutral, or Positive
    """
    if not text.strip():
        return {"score": 0, "label": "Neutral"}

    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity  # Sentiment polarity (-1 to 1)

    # Assign a sentiment label based on score
    if sentiment_score > 0.1:
        sentiment_label = "Positive"
    elif sentiment_score < -0.1:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    return {"score": sentiment_score, "label": sentiment_label}

# Example usage
if __name__ == "__main__":
    sample_text = "The economy is crashing, and things are getting worse!"
    result = analyze_sentiment(sample_text)
    print(f"Sentiment Score: {result['score']}, Label: {result['label']}")
