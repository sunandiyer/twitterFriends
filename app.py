#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 13:42:35 2017

@author: sunandiyer
"""

import tweepy
from tweepy import OAuthHandler
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    consumer_key = "1vnx8rybX0CvnERfLOfZRkJmN"
    consumer_secret = 'pYSzrmJqlLT3A8znLBpSzt3djC0NwGAIDctLeJevHOIX9KBlfM'
    access_token = '1478601054-yjTbHT3FJdLCleRbZnnmFcsqkIroSKeKqZROCPw'
    access_secret = 'cHKGTKWcEds0q6FjdwJPV01qt6L2bhvFTuQAxWtdDHHFj'
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
     
    api = tweepy.API(auth)
    me = api.me()
    #return str(me.id)
    entries = ["1", "2", "3"]
    
    #friends = [str(api.get_user(x).screen_name) for x in api.followers_ids(me.id)][:10]
    
    friends = ', '.join(str(api.get_user(x).screen_name) for x in api.followers_ids(me.id))
    #print(friends)
    #return str(api.followers_ids(me.id)[0])
    #str(followers(me.id)
    #return friends
    return render_template('temp.html', entries=friends)
    #return render_template('main.html', entries=entries)

if __name__ == "__main__":
        app.debug = True
        app.run()
         
         
         
