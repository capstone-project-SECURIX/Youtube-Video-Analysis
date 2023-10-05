# dataset link : https://www.kaggle.com/datasets/datasnaek/youtube-new/data

# app.py (main Flask application)

from flask import Flask, render_template, request
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
df1 = pd.read_csv(r"static/datasets/USvideos.csv")
df2 = pd.read_csv(r"static/datasets/USvideos.csv")
df3 = pd.read_csv(r"static/datasets/USvideos.csv")
df4 = pd.read_csv(r"static/datasets/USvideos.csv")

# Dummy dataset options
datasets = ['set1', 'set2', 'set3']

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
@app.route('/Top_5_Categories_with_Most_Videos', methods=['GET'])
def search():
    selected_dataset = request.form.get('dataset')

    if selected_dataset == ''
    results =  { 
        'Top_5_Categories_with_Most_Videos' :Top_5_Categories_with_Most_Videos(df1), 
        'Top_10_Liked_Videos' :Top_10_Liked_Videos(df1), 
        'Top_10_Most_Viewed_Videos' :Top_10_Most_Viewed_Videos(df1), 
        'correlation_between' :correlation_between(df1), 
                } 
    
    return render_template('displayData.html', results=results)







# @app.route('/video/<video_id>')
# def video_details(video_id):
#     # Retrieve details for the selected video
#     video_details = data[data['video_id'] == video_id].iloc[0]
#     return render_template('video_details.html', video=video_details)



if __name__ == '__main__':
    app.run(debug=True)
