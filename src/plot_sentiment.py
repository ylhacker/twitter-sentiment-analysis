import matplotlib.pyplot as plt

def plot_sentiment(df, topic):
    sentiment_counts = df["Sentiment"].value_counts()

    plt.figure(figsize=(6, 4))
    sentiment_counts.plot(kind="bar", color=["green", "red", "gray"])
    plt.title(f"Sentiment Analysis on '{topic}'")
    plt.xlabel("Sentiment")
    plt.ylabel("Tweet Count")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("data/sentiment_plot.png")
    plt.show()
