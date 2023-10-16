# dataset link : https://www.kaggle.com/datasets/datasnaek/youtube-new/data

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

from utils import Top_5_Categories_with_Most_Videos, Top_10_Liked_Videos, Top_10_Most_Viewed_Videos, correlation_between, channel_Top_10_Liked_Videos, channel_Top_Viewed_Video, channel_Top_Impression_Video, channel_Total_Videos


app = Flask(__name__)

file_paths = [
    r"static/datasets/USvideos.csv",
    r"static/datasets/RUvideos.csv",
    r"static/datasets/CAvideos.csv",
    r"static/datasets/DEvideos.csv",
    r"static/datasets/INvideos.csv"
]

datasets = ['USvideos', 'RUvideos', 'CAvideos', 'DEvideos', 'INvideos']

@app.route('/')
def index():
    return render_template('index.html', datasets=datasets)

@app.route('/dataset', methods=['GET', 'POST'])
def search():

    if request.method == 'POST':

        selected_dataset = request.form.get('dataset')
        # df = pd.read_csv(file_paths[0],  encoding='latin1')

        if selected_dataset == 'USvideos':
            df = pd.read_csv(file_paths[0],  encoding='latin1')
        elif selected_dataset == 'RUvideos':
            df = pd.read_csv(file_paths[1],  encoding='latin1')
        elif selected_dataset == 'CAvideos':
            df = pd.read_csv(file_paths[2],  encoding='latin1')
        elif selected_dataset == 'DEvideos':
            df = pd.read_csv(file_paths[3],  encoding='latin1')
        elif selected_dataset == 'INvideos':
            df = pd.read_csv(file_paths[4],  encoding='latin1')

        results =  { 
            'Top_5_Categories_with_Most_Videos' :Top_5_Categories_with_Most_Videos(df), 
            'Top_10_Liked_Videos' :Top_10_Liked_Videos(df), 
            'Top_10_Most_Viewed_Videos' :Top_10_Most_Viewed_Videos(df), 
            'correlation_between' :correlation_between(df), 
                    } 
        
        return render_template('index.html', results=results, datasets=datasets)
    

    elif request.method == 'GET':
        # print("POST request")
        return redirect(url_for('index'))


@app.route('/channel', methods=['GET', 'POST'])
def channel():
    if request.method == 'POST':

        selected_dataset = request.form.get('dataset')
        channel_title = request.form.get('channel')
        # df = pd.read_csv(file_paths[0],  encoding='latin1')

        if selected_dataset == 'USvideos':
            df = pd.read_csv(file_paths[0],  encoding='latin1')
        elif selected_dataset == 'RUvideos':
            df = pd.read_csv(file_paths[1],  encoding='latin1')
        elif selected_dataset == 'CAvideos':
            df = pd.read_csv(file_paths[2],  encoding='latin1')
        elif selected_dataset == 'DEvideos':
            df = pd.read_csv(file_paths[3],  encoding='latin1')
        elif selected_dataset == 'INvideos':
            df = pd.read_csv(file_paths[4],  encoding='latin1')

        results =  { 
            'channel_Top_10_Liked_Videos' :channel_Top_10_Liked_Videos(df, channel_title), 
            'channel_Top_Viewed_Video' :channel_Top_Viewed_Video(df, channel_title), 
            'channel_Top_Impression_Video' :channel_Top_Impression_Video(df, channel_title), 
            'channel_Total_Videos' :channel_Total_Videos(df, channel_title), 
                    } 

        return render_template('channelData.html', results=results, datasets=datasets, channel_title=channel_title)

    elif request.method == 'GET':
        # print("POST request")
        return render_template('channelData.html', datasets=datasets)

'''
Top_5_Categories_with_Most_Videos:  [{'cat': 'Entertainment', 'count': 13451}, {'cat': 'News & Politics', 'count': 4159}, {'cat': 'People & Blogs', 'count': 4105}, {'cat': 'Comedy', 'count': 3773}, {'cat': 'Music', 'count': 3731}]
'''

@app.route('/rlang', methods=['GET'])
def rlang():
    return render_template('rlang.html', datasets=datasets)





# @app.route('/video/<video_id>')
# def video_details(video_id):
#     # Retrieve details for the selected video
#     video_details = data[data['video_id'] == video_id].iloc[0]
#     return render_template('video_details.html', video=video_details)



if __name__ == '__main__':
    app.run(debug=True)
