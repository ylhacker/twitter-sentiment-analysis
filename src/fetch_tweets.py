import tweepy
import pandas as pd

def fetch_tweets(bearer_token, query, max_results=100):
    client = tweepy.Client(bearer_token=bearer_token)
    query = f"{query} lang:en -is:retweet"

    response = client.search_recent_tweets(
        query=query,
        max_results=max_results,
        tweet_fields=["created_at", "text"]
    )

    if not response.data:
        return pd.DataFrame(columns=["Time", "Tweet"])

    tweets_data = [[tweet.created_at, tweet.text] for tweet in response.data]
    return pd.DataFrame(tweets_data, columns=["Time", "Tweet"])
