#!/usr/bin/python
# -*- coding:UTF-8 -*-

#import sys
#from urllib import urlencode
from oauth2 import Client, Consumer, Token
#import twitter
import tweepy2
consumer_key = "5m0qb8v77T1YvmkPl01opg"
consumer_secret = "EjoNbCyyMaWvcS31XxswJC4NRnQfpJnQIpCnYjo0"
user_key = "418515557-CSqxX1WDyirMNoq5BkwOyInRFZFwBBBw79soPPp3"
user_secret = "hIGd41L5CJeIexK6lvmOtwzSfhkmV1GLGpxWgr1u8"
auth = tweepy2.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(user_key, user_secret)
client = Client(Consumer(consumer_key, consumer_secret),
                Token(user_key, user_secret))
api = tweepy2.API(auth)
