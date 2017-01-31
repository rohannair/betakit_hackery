import csv
import os
import time
import tweepy

from os.path import join, dirname
from pprint import pprint
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")

access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweepy_cursor = tweepy.Cursor(api.search, q="@ddebow").items():
def grab_tweets:
  while True:
    try:
      for tweet in tweepy_cursor
        if (tweet.in_reply_to_status_id_str == "826164031455162368"):
          last_tweet = tweet.id
          tweet_url = "http://twitter.com/%s/status/%s" % tweet.user.screen_name, tweet.id

          f = open('file.csv', 'wb')
          w = csv.writer(f)
          w.writeRows(tweet_url)
          f.close()

      time.sleep(60 * 30)

    except StopIteration:
      break


