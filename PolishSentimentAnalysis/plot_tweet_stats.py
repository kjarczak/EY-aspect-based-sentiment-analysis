from operator import attrgetter
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, DateFormatter
import numpy as np
from pandas import DataFrame
from datetime import timedelta
from tweets_mock import get_tweets


width = 8
height = 6
dpi = 120


def plot_average(tweets: list):
    if len(tweets) < 1:
        return

    hashtag = tweets[0].hashtag
    df = DataFrame([tweet.to_dict() for tweet in tweets])
    df = df.drop(columns=['hashtag', 'content'])
    df = df.groupby('creation_date').aggregate('mean')
    df = df.reset_index()
    plt.plot(df['creation_date'], df['sentiment'])
    ax = plt.gca()
    ax.xaxis.set_major_locator(DayLocator(interval=1))
    ax.xaxis.set_major_formatter(DateFormatter('%d-%m-%Y'))
    plt.gcf().autofmt_xdate()
    plt.xlabel('Date')
    plt.ylabel('Average sentiment')
    plt.title(hashtag)
    plt.figure(figsize=(width, height), dpi=dpi)
    plt.show()

    return plt


def plot_counts(tweets: list):
    if len(tweets) < 1:
        return

    min_date = min(tweets, key=attrgetter('creation_date')).creation_date
    max_date = max(tweets, key=attrgetter('creation_date')).creation_date
    df = DataFrame([tweet.to_dict() for tweet in tweets])
    df = df.drop(columns=['hashtag', 'content'])
    df = df.groupby(['creation_date', 'sentiment']).size()
    df = df.to_frame('counts').reset_index()
    for creation_date in df['creation_date'].unique():
        if df.loc[(df['creation_date'] == creation_date) & (df['sentiment'] == -1)].empty:
            df = df.append({'creation_date': creation_date, 'sentiment': -1, 'counts': 0}, ignore_index=True)
        if df.loc[(df['creation_date'] == creation_date) & (df['sentiment'] == 0)].empty:
            df = df.append({'creation_date': creation_date, 'sentiment': 0, 'counts': 0}, ignore_index=True)
        if df.loc[(df['creation_date'] == creation_date) & (df['sentiment'] == 1)].empty:
            df = df.append({'creation_date': creation_date, 'sentiment': 1, 'counts': 0}, ignore_index=True)
    df.sort_values(by=['creation_date', 'sentiment'], inplace=True)
    x = np.arange((max_date - min_date).days + 1)
    negative = list(df['counts'].where(df['sentiment'] == -1).dropna().to_frame('counts')['counts'])
    neutral = list(df['counts'].where(df['sentiment'] == 0).dropna().to_frame('counts')['counts'])
    positive = list(df['counts'].where(df['sentiment'] == 1).dropna().to_frame('counts')['counts'])
    bar_neg = plt.bar(x, negative, 0.35)
    bar_neutral = plt.bar(x, neutral, 0.35, bottom=negative)
    bar_pos = plt.bar(x, positive, 0.35, bottom=np.add(negative, neutral))
    plt.xlabel('Date')
    plt.ylabel('Tweet count with sentiment')
    plt.xticks(x, [min_date + timedelta(days=i) for i in range(0, len(x))], rotation=45)
    plt.legend((bar_neg[0], bar_neutral[0], bar_pos[0]), ('Negative', 'Neutral', 'Positive'), loc='upper center',
               bbox_to_anchor=(0.5, -0.25))
    plt.title(tweets[0].hashtag)
    plt.show()

    return plt

