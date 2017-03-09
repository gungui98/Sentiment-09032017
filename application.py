from flask import Flask, redirect, render_template, request, url_for

import helpers
from analyzer import Analyzer
import sys
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "").lstrip("@")
    if not screen_name:
        return render_template("error index.html")
        

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name)
    
    if tweets==[]:
        return render_template("error index.html")
        
    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")

    # instantiate analyzer
    analyzer = Analyzer(positives, negatives)
    positive, negative, neutral=0.0,0.0,0.0
    for tweet in tweets:
        temp =analyzer.analyze(tweet)
        if temp>0 :
            positive+=1
        elif temp<0 :
            negative+=1
        else :
            neutral+=1
    # generate chart
    chart = helpers.chart(positive/(positive+negative+neutral), negative/(positive+negative+neutral), neutral/(positive+negative+neutral))

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
