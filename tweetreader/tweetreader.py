from __future__ import print_function
import os
import sys
import tweepy
from requests.packages.urllib3 import exceptions
import warnings
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, Markup

warnings.filterwarnings(action='ignore', category=exceptions.InsecurePlatformWarning)

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
                       TITLE = 'ALMA Engineering Test robot tweet reader',
                       REFRESH_RATE_MINS = 5,
                       DEV_MODE = False
                      )
                 )
app.config.from_pyfile('application.cfg', silent=True)

def GetLatestTweets():
    if not app.config['DEV_MODE']:
        auth = tweepy.OAuthHandler(app.config['CONSUMER_KEY'], app.config['CONSUMER_SECRET'])
        auth.set_access_token(app.config['ACCESS_TOKEN'], app.config['ACCESS_TOKEN_SECRET'])
        api = tweepy.API(auth)

        # Get latest 20 tweets by defined user
        latest_tweets = api.home_timeline()
    else:
        print('DEV MODE')
        import pickle
        with open('test_tweets.pkl', 'r') as f:
            latest_tweets = pickle.load(f)
    return latest_tweets

@app.route('/')
def DisplayMainPage():
    # Get latest 20 tweets by defined user
    latest_tweets = GetLatestTweets()

    return render_template('show_tweets.html', tweets=latest_tweets, include_layout=True)

@app.route('/latest')
def LatestTweets():
    # Get latest 20 tweets by defined user
    latest_tweets = GetLatestTweets()

    return render_template('show_tweets.html', tweets=latest_tweets, include_layout=False)

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page_not_found.html'), 404
