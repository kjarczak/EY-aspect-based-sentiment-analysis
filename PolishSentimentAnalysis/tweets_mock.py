from tweet import Tweet
from datetime import datetime, timedelta
from random import randint, choices, choice
import string
from math import ceil


def get_tweets(hashtag, count, since, until):
    days_delta = timedelta(days=randint(5, 7))
    min_date = datetime.now().date() - days_delta
    max_date = datetime.now().date()
    tweets_per_day = ceil(count / days_delta.days)

    tweets = list()
    population = [-1, 0, 1]
    for i in range(0, days_delta.days):
        creation_time = min_date + timedelta(days=i)
        for j in range(0, tweets_per_day):
            weights = [0.25, 0.6, 0.15]
            tweet = Tweet(hashtag=hashtag, creation_date=creation_time,
                          content=''.join(choice(string.ascii_letters) for k in range(30, 140)),
                          sentiment=choices(population, weights)[0])
            tweets.append(tweet)

    return tweets
