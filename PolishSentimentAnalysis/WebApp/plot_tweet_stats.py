import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, DateFormatter
import numpy as np
from pandas import DataFrame
from datetime import timedelta
import io
from dateutil import parser


width = 4
height = 3
dpi = 120
plt.figure(figsize=(width, height), dpi=dpi)


def plot_average(df):
    plt.clf()
    if isinstance(df, dict):
        df = DataFrame(df)

    hashtag = df['hashtag'].iloc[0]
    df = df.drop(columns=['hashtag', 'content'])
    df['creation_date'] = [parser.parse(creation_date).date() for creation_date in df['creation_date']]
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

    return get_image_bytes(plt)


def plot_counts(df):
    plt.clf()
    if isinstance(df, dict):
        df = DataFrame(df)
    hashtag = df['hashtag'].iloc[0]
    df['creation_date'] = [parser.parse(creation_date).date() for creation_date in df['creation_date']]
    min_date = min(df['creation_date'])
    max_date = max(df['creation_date'])
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
    plt.title(hashtag)

    return get_image_bytes(plt)


def get_image_bytes(plot):
    output = io.BytesIO()
    plot.savefig(output, format='png')

    return output.getvalue()

