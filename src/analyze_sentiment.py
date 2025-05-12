from textblob import TextBlob

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

def analyze_sentiment(df):
    df["Sentiment"] = df["Tweet"].apply(get_sentiment)
    return df
