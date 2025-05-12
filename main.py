from src.fetch_tweets import fetch_tweets
from src.analyze_sentiment import analyze_sentiment
from src.plot_sentiment import plot_sentiment

# Replace with your bearer token from the Twitter Developer Portal
bearer_token = "AAAAAAAAAAAAAAAAAAAAANfa1AEAAAAABsPAb4WBcobCvEWONMvmfNutirY%3DIWCkBQufMeH3Ug4J94BVME5SkQrbIBQJIZnKajEYcoyTiwjni4"

# Topic to search
topic = "Kenya elections"

# Step 1: Fetch tweets
df = fetch_tweets(bearer_token, topic, max_results=100)

# Step 2: Analyze sentiment
df = analyze_sentiment(df)

# Step 3: Save to CSV
df.to_csv("data/sentiment_analysis_results.csv", index=False)

# Step 4: Plot sentiment
plot_sentiment(df, topic)
