# dataset link : https://www.kaggle.com/datasets/datasnaek/youtube-new/data

# app.py (main Flask application)

from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns

import warnings
from collections import Counter
import datetime
import wordcloud
import json

from utils import Top_5_Categories_with_Most_Videos, Top_10_Liked_Videos, Top_10_Most_Viewed_Videos, correlation_between

# print("Top_5_Categories_with_Most_Videos: ",Top_5_Categories_with_Most_Videos(df))
# print("Top_10_Liked_Videos: ",Top_10_Liked_Videos(df))
# print("Top_10_Most_Viewed_Videos: ",Top_10_Most_Viewed_Videos(df))
# print("correlation_between: ",correlation_between(df))


# Hiding warnings for cleaner display
# warnings.filterwarnings('ignore')

# Configuring some options
# %matplotlib inline
# %config InlineBackend.figure_format = 'retina'
# If you want interactive plots, uncomment the next line
# %matplotlib notebook

app = Flask(__name__)


# Load your dataset using Pandas

file_paths = [
    r"static/datasets/USvideos.csv",
    r"static/datasets/RUvideos.csv",
    r"static/datasets/CAvideos.csv",
    r"static/datasets/DEvideos.csv"
]

# Dummy dataset options
datasets = ['USvideos', 'RUvideos', 'CAvideos', 'DEvideos']

# Define routes and views
@app.route('/')
def index():
    return render_template('index.html', datasets=datasets)

# @app.route('/search', methods=['GET', 'POST'])
# def search():
#     # Implement search and filter logic here
#     results = "123"
#     return render_template('search.html', results=results)

# print("Top_5_Categories_with_Most_Videos: ",Top_5_Categories_with_Most_Videos(df))
@app.route('/dataset', methods=['GET', 'POST'])
def search():

    if request.method == 'POST':

        selected_dataset = request.form.get('dataset')

        if selected_dataset == 'USvideos':
            df = file_paths[0]
        elif selected_dataset == 'RUvideos':
            df = file_paths[1]
        elif selected_dataset == 'CAvideos':
            df = file_paths[2]
        elif selected_dataset == 'DEvideos':
            df = file_paths[3]

        results =  { 
            'Top_5_Categories_with_Most_Videos' :Top_5_Categories_with_Most_Videos(df), 
            'Top_10_Liked_Videos' :Top_10_Liked_Videos(df), 
            'Top_10_Most_Viewed_Videos' :Top_10_Most_Viewed_Videos(df), 
            'correlation_between' :correlation_between(df), 
                    } 
        
        return render_template('index.html', results=results)
    

    elif request.method == 'GET':
        # print("POST request")
        return redirect(url_for('index'))








# @app.route('/video/<video_id>')
# def video_details(video_id):
#     # Retrieve details for the selected video
#     video_details = data[data['video_id'] == video_id].iloc[0]
#     return render_template('video_details.html', video=video_details)



if __name__ == '__main__':
    app.run(debug=True)
