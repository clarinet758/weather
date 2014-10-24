#!/usr/bin/python
# -*- coding:UTF-8 -*-

from urllib import urlencode
from oauth2 import Client, Consumer, Token
import tweepy

consumer_key = "xxxxxx"
consumer_secret = "xxxxxxxxxxx"
user_key = "*****-xxxxxxxxxx"
user_secret = "xxxxxxxxx"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(user_key, user_secret)
client = Client(Consumer(consumer_key, consumer_secret), Token(user_key, user_secret))
api = tweepy.API(auth)
ep = "https://api.twitter.com/1.1/statuses/update.json"

def tweet(message):
    client.request(ep, 'POST', urlencode({'status': message}))


def reply(message, ids):
    client.request(ep, 'POST', urlencode({'status': message, 'in_reply_to_status_id': ids}))
