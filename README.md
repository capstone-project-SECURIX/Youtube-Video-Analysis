# YouTube Video Analysis

This project analyzes YouTube video datasets to gain insights into categories, video popularity, correlations, and channel-specific metrics. It includes a Flask web application for interacting with the data.

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Analysis Functions](#analysis-functions) 
- [Flask App](#flask-app)
- [Datasets](#datasets)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## About 

This project utilizes Python, Flask, and R to analyze YouTube trending video datasets from multiple countries. The goal is to explore categories, popularity metrics, correlations, and channel-specific analytics. An interactive Flask app allows users to select datasets and view analysis results.

Key features:

- Top categories by video count 
- Top 10 liked/viewed videos
- Correlations between views, likes, dislikes, comments
- Channel-specific analytics
- R scripts for data analysis
- Flask app for interacting with data

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Pandas 
- NumPy
- Matplotlib
- Seaborn
- WordCloud

```bash
pip install flask pandas numpy matplotlib seaborn wordcloud
```

### Installation

```bash
git clone https://github.com/capstone-project-SECURIX/Youtube-Video-Analysis.git
cd youtube-video-analysis
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```

The Flask app will be available at http://localhost:5000. Select a dataset and explore the video analytics.

## Code Structure

    .
    ├── static/
    │   ├── datasets/        # CSV datasets
    │   ├── images/          # Generated images  
    │   └── styles/          # CSS files
    │
    ├── templates/           # HTML templates
    │
    ├── youtube-dataset/     # Raw dataset files
    │
    ├── analyze_youtube_data.r    # R analysis scripts
    ├── app.py               # Flask app
    ├── utils.py             # Python analysis functions
    ├── requirements.txt
    └── README.md

## Analysis Functions

Located in `analyze_youtube_data.r` and `utils.py`:

- `top_categories()`: Get top categories by video count
- `top_liked_videos()`: Get top 10 liked videos
- `top_viewed_videos()`: Get top 10 viewed videos  
- `correlation()`: View correlations between metrics
- `channel_top_liked()`: Get top liked for channel
- `channel_top_viewed()`: Get most viewed video for channel
- ...more

## Flask App

`app.py` handles routes and serves analysis results to the template files.

- `/` - Homepage, select dataset
- `/dataset` - Display analysis for selected dataset
- `/channel` - Display channel-specific analytics
- `/rlang` - Display R code

## Datasets

The `youtube-dataset/` folder contains CSV files for different countries:

- USvideos.csv
- RUvideos.csv 
- CAvideos.csv
- DEvideos.csv
- INvideos.csv

## Acknowledgements

- [Kaggle Dataset](https://www.kaggle.com/datasets/datasnaek/youtube-new)
- [Kaggle Notebook](https://www.kaggle.com/code/mrappplg/youtube-trending-videos-analysis)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.