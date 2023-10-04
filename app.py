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

# Hiding warnings for cleaner display
warnings.filterwarnings('ignore')

# Configuring some options
# %matplotlib inline
# %config InlineBackend.figure_format = 'retina'
# If you want interactive plots, uncomment the next line
# %matplotlib notebook

app = Flask(__name__)

# Load your dataset using Pandas
df = pd.read_csv(r"static/datasets/USvideos.csv")

# Define routes and views
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    # Implement search and filter logic here
    results = "123"
    return render_template('search.html', results=results)

# @app.route('/video/<video_id>')
# def video_details(video_id):
#     # Retrieve details for the selected video
#     video_details = data[data['video_id'] == video_id].iloc[0]
#     return render_template('video_details.html', video=video_details)

if __name__ == '__main__':
    app.run(debug=True)
