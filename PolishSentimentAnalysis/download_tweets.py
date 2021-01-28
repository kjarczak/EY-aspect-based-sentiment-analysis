import tweepy
import pandas as pd
from dotenv import load_dotenv
from dateutil import parser
import os
from datetime import date, timedelta
from math import ceil
from random import choices

load_dotenv()
consumer_secret = os.getenv('CONSUMER_SECRET')
consumer_key = os.getenv('CONSUMER_KEY')
# access_token = os.getenv('ACCESS_TOKEN')
# access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
max_api_requests = int(os.getenv('MAX_API_REQUESTS'))
max_days_until = int(os.getenv('MAX_DAYS_UNTIL'))
language = 'pl'

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def get_tweets(hashtag, count, since, until):
    hashtag, count, since, until, tweets_per_day, days_count = prepare(hashtag, count, since, until)
    tweets = list()
    for i in range(0, days_count):
        tweets_cursor = tweepy.Cursor(api.search, q=hashtag, lang=language,
                                      since=str(until - timedelta(days=days_count - i)),
                                      until=str(until - timedelta(days=days_count - i - 1)),
                                      tweet_mode='extended').items(tweets_per_day)
        tweets.extend(tweets_cursor)

    return pd.DataFrame([{'hashtag': hashtag, 'creation_date': tweet._json['created_at'],
                          'content': tweet._json['full_text']} for tweet in tweets])


def prepare(hashtag, count, since, until):
    if not isinstance(count, int):
        count = int(count)

    if count > max_api_requests:
        raise Exception('Too much tweets requested at once')

    if not isinstance(since, date):
        since = parser.parse(since).date()

    if since < date.today() - timedelta(days=max_days_until):
        raise Exception('Can search only in previous {} days'.format(max_days_until))

    if not isinstance(until, date):
        until = parser.parse(until).date()

    if until > date.today():
        raise Exception('Date {} is later than today {}'.format(since, date.today()))

    if since > until:
        raise Exception('Given dates are incorrect, since [{}] is later than until [{}]'.format(since, until))

    if not hashtag.startswith('#'):
        hashtag = '#{}'.format(hashtag)

    days_count = (until - since).days
    tweets_per_day = ceil(count / float(days_count))

    return hashtag, count, since, until, tweets_per_day, days_count


def mock_sentiment(df):
    count = len(df.index)
    weights = [0.25, 0.6, 0.15]
    population = [-1, 0, 1]
    sentiment = [choices(population, weights) for i in range(0, count)]
    df['sentiment'] = sentiment
    
    return df
