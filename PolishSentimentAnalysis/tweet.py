from dateutil import parser
from datetime import date
import json


class Tweet:
    def __init__(self, hashtag: str, creation_date, content: str, sentiment: int = None):
        if not hashtag.startswith('#'):
            hashtag = '#{}'.format(hashtag)
        self.hashtag = hashtag

        if not isinstance(creation_date, date):
            creation_date = parser.parse(creation_date).date()
        self.creation_date = creation_date

        self.content = content
        self.sentiment = sentiment

    def to_json(self):
        self.creation_date = str(self.creation_date)
        return json.dumps(self.to_dict(), ensure_ascii=False)

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls.from_dict(data)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    @classmethod
    def from_tweet_api_obj(cls, hashtag, tweet_obj, sentiment=None):
        return cls(hashtag, tweet_obj._json['created_at'], tweet_obj._json['full_text'], sentiment)
