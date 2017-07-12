
from __future__ import print_function
import os
import sys
import tweepy
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, Markup

app = Flask(__name__, instance_relative_config=True) # create the application instance :)
app.config.from_object(__name__) # load config from this file

# Load default config and override config from instance folder file second (if existing)
app.config.update(dict(
                       # Access tokens for user 'ALMAEngTest'
                       CONSUMER_KEY        = 'Get from https://dev.twitter.com/',
                       CONSUMER_SECRET     = 'Get from https://dev.twitter.com/',
                       ACCESS_TOKEN        = 'Get from https://dev.twitter.com/',
                       ACCESS_TOKEN_SECRET = 'Get from https://dev.twitter.com/'  ,
                       SECRET_KEY = 'V0tISH0cy1pGyynHyfKI',
                       TITLE = 'AMGEngTest robot tweet reader'
                      )
                 )
app.config.from_pyfile('application.cfg', silent=True)

@app.route('/')
def DisplayTweets():
  auth = tweepy.OAuthHandler(app.config['CONSUMER_KEY'], app.config['CONSUMER_SECRET'])
  auth.set_access_token(app.config['ACCESS_TOKEN'], app.config['ACCESS_TOKEN_SECRET'])
  api = tweepy.API(auth)

  public_tweets = api.home_timeline()
  # for tweet in public_tweets:
  #     print(tweet.text)
  print(public_tweets[0])
  return render_template('show_tweets.html', tweets=public_tweets)

# @app.errorhandler(404)
# def pageNotFound(error):
#     return render_template('page_not_found.html'), 404
