# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 10:10:00 2018

@author: Alexey
"""

import tweepy
from tweepy import OAuthHandler
import twitter

import re

consumer_key='tuuPxYC2QYqMqCor41TuLlEWV'
consumer_secret='NMeqN2w0KhnkbT4CFk3ef3Oi7SR1NlfLfQV3OnQtUwkd8czam0'
access_token_key='2809175323-8rlwmRgpkYed0E9Lb36V7VxoIlBaULlUyAJtdNA'
access_token_secret='LbwpuZZWpxichjGXJS3TmBYLY2COyofjnb2KyrOj2b02h'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(1):
    print(status.text)

# PARSE HTML

# save url
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup as bs

url = 'https://www.house.gov/representatives'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
the_page = response.read()

f = open('my_us_rep.html', 'w')
f.write(bs(the_page, 'html.parser').prettify())
f.close


#t="A fat cat doesn't 7at oat but a rat e99ats bats."
#mo = re.findall("[0-9]at", t)
#print(mo)