#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 13:42:35 2017

@author: sunandiyer
"""

import tweepy
from tweepy import OAuthHandler
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
app.secret_key = "XX"

@app.route('/', methods = ['GET', 'POST'])
def main():
    error = None
    if request.method == 'POST':
        username1 = request.form['user1']
        username2 = request.form['user2']
        session['user1'] = username1
        session['user2'] = username2
        return redirect('temp')
    return render_template('main.html', error = error)

@app.route("/temp", methods = ['GET', 'POST'])
def show_entries():
    
            
        
        consumer_key = "1vnx8rybX0CvnERfLOfZRkJmN"
        consumer_secret = 'pYSzrmJqlLT3A8znLBpSzt3djC0NwGAIDctLeJevHOIX9KBlfM'
        access_token = '1478601054-yjTbHT3FJdLCleRbZnnmFcsqkIroSKeKqZROCPw'
        access_secret = 'cHKGTKWcEds0q6FjdwJPV01qt6L2bhvFTuQAxWtdDHHFj'
        
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        
        api = tweepy.API(auth)
        
        user1 = api.get_user(session['user1'])
        user2 = api.get_user(session['user2'])
        
        user1Followers = list(str(api.get_user(x).screen_name) for x in api.followers_ids(user1.id))
        user2Followers = list(str(api.get_user(x).screen_name) for x in api.followers_ids(user2.id))
        
        entries = list(set(user1Followers) & set(user2Followers))
        
        return render_template('temp.html', entries = entries)
        
        
    


'''@app.route("/user")
def show_entries():
    
    consumer_key = "1vnx8rybX0CvnERfLOfZRkJmN"
    consumer_secret = 'pYSzrmJqlLT3A8znLBpSzt3djC0NwGAIDctLeJevHOIX9KBlfM'
    access_token = '1478601054-yjTbHT3FJdLCleRbZnnmFcsqkIroSKeKqZROCPw'
    access_secret = 'cHKGTKWcEds0q6FjdwJPV01qt6L2bhvFTuQAxWtdDHHFj'
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
     
    api = tweepy.API(auth)
    me = api.me()
    #return str(me.id)
    
    #friends = [str(api.get_user(x).screen_name) for x in api.followers_ids(me.id)][:10]
    
    friends = list(str(api.get_user(x).screen_name) for x in api.followers_ids(me.id))
    #print(friends)
    #return str(api.followers_ids(me.id)[0])
    #str(followers(me.id)
    #return friends
    return render_template('temp.html', entries=friends)
'''    

if __name__ == "__main__":
        app.debug = True
        app.run()
         
         
         
