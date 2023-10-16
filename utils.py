import pandas as pd
import numpy as np
import json


# import matplotlib as mpl
# from matplotlib import pyplot as plt
# import seaborn as sns

# import warnings
# from collections import Counter
# import datetime
# import wordcloud
# import json

file_paths = [
    r"static/datasets/USvideos.csv",
    r"static/datasets/RUvideos.csv",
    r"static/datasets/CAvideos.csv",
    r"static/datasets/DEvideos.csv"
]

csvfilepath = file_paths[3]
# print("csvfilepath : ",csvfilepath)
df = pd.read_csv(csvfilepath,  encoding='latin1')

category_mapping = {
    1: 'Film & Animation',
    2: 'Autos & Vehicles',
    10: 'Music',
    15: 'Pets & Animals',
    17: 'Sports',
    18: 'Short Movies',
    19: 'Travel & Events',
    20: 'Gaming',
    21: 'Videoblogging',
    22: 'People & Blogs',
    23: 'Comedy',
    24: 'Entertainment',
    25: 'News & Politics',
    26: 'Howto & Style',
    27: 'Education',
    28: 'Science & Technology',
    29: 'Nonprofits & Activism',
    30: 'Movies',
    31: 'Anime/Animation',
    32: 'Action/Adventure',
    33: 'Classics',
    34: 'Comedy',
    35: 'Documentary',
    36: 'Drama',
    37: 'Family',
    38: 'Foreign',
    39: 'Horror',
    40: 'Sci-Fi/Fantasy',
    41: 'Thriller',
    42: 'Shorts',
    43: 'Shows',
    44: 'Trailers'
}


def Top_5_Categories_with_Most_Videos(df):
    # Get the top 5 categories and their counts
    top_categories = df['category_id'].value_counts().head(5)

    # Convert to a list of key-value pairs and map category IDs to names
    category_list = [(category_mapping.get(cat_id, 'Unknown'), count) for cat_id, count in top_categories.items()]

    jsondata = [{'cat': category, 'count': count} for category, count in category_list]
    # for item in jsondata:
        # print("cat: ", item['cat'], "count: ", item['count'])

    # {'cat': 'Howto & Style', 'count': 4146}
    return jsondata



def Top_10_Liked_Videos(df):
    top_rated_videos = df.nlargest(10, 'likes')

    jsondata = []

    for index, row in top_rated_videos.iterrows():
        video_info = {'title': row['title'], 'likes': row['likes']}
        jsondata.append(video_info)

    # Print the resulting JSON data
    for item in jsondata:
        print(item)

    # {'title': "BTS (방탄소년단) 'FAKE LOVE' Official MV", 'likes': 5053329}
    return jsondata

def Top_10_Most_Viewed_Videos(df):
    top_viewed_videos = df.nlargest(10, 'views')

    jsondata = []

    for index, row in top_viewed_videos.iterrows():
        video_info = {'title': row['title'], 'views': row['views']}
        jsondata.append(video_info)

    # Print the resulting JSON data
    for item in jsondata:
        print(item)

    # {'title': 'Childish Gambino - This Is America (Official Video)', 'views': 225211923}
    return jsondata


# Determine the correlation between the number of views, likes, dislikes, and comments on videos.
def correlation_between(df):
    # Assuming you have already calculated the correlation matrix
    correlation_matrix = df[['views', 'likes', 'dislikes', 'comment_count']].corr()

    # Convert the correlation matrix to a JSON string
    correlation_json = correlation_matrix.to_json(orient='split')

    # Now, parse the JSON string to a Python dictionary
    correlation_data = json.loads(correlation_json)

    # Print the correlation data (for testing purposes)
    # print(correlation_data)

    # correlation_between:  {'columns': ['views', 'likes', 'dislikes', 'comment_count'], 'index': ['views', 'likes', 'dislikes', 'comment_count'], 'data': [[1.0, 0.8491765212, 0.4722132456, 0.6176212718], [0.8491765212, 1.0, 0.4471864632, 0.8030568578], [0.4722132456, 0.4471864632, 1.0, 0.7001836236], [0.6176212718, 0.8030568578, 0.7001836236, 1.0]]}
    
    return correlation_data


# print("Top_5_Categories_with_Most_Videos: ",Top_5_Categories_with_Most_Videos(df))
# print("\n\n")
# print("Top_10_Liked_Videos: ",Top_10_Liked_Videos(df))
# print("\n\n")

# print("Top_10_Most_Viewed_Videos: ",Top_10_Most_Viewed_Videos(df))
# print("\n\n")

# print("correlation_between: ",correlation_between(df))


'''

Top_5_Categories_with_Most_Videos:  [{'cat': 'Entertainment', 'count': 15292}, {'cat': 'People & Blogs', 'count': 5988}, {'cat': 'News & Politics', 'count': 2935}, {'cat': 'Sports', 'count': 2752}, {'cat': 'Comedy', 'count': 2534}]

{'title': "BTS (ë°©í\x83\x84ì\x86\x8cë\x85\x84ë\x8b¨) 'FAKE LOVE' Official MV", 'likes': 4924056}
{'title': "BTS (ë°©í\x83\x84ì\x86\x8cë\x85\x84ë\x8b¨) 'FAKE LOVE' Official MV", 'likes': 4750254}
{'title': "BTS (ë°©í\x83\x84ì\x86\x8cë\x85\x84ë\x8b¨) 'FAKE LOVE' Official MV", 'likes': 4470888}
{'title': "BTS (ë°©í\x83\x84ì\x86\x8cë\x85\x84ë\x8b¨) 'FAKE LOVE' Official MV", 'likes': 3880074}
{'title': 'YouTube Rewind: The Shape of 2017 | #YouTubeRewind', 'likes': 2811217}
{'title': 'YouTube Rewind: The Shape of 2017 | #YouTubeRewind', 'likes': 2656675}
{'title': "Marvel Studios' Avengers: Infinity War Official Trailer", 'likes': 2513103}
{'title': 'Childish Gambino - This Is America (Official Video)', 'likes': 2478908}
{'title': "BTS (ë°©í\x83\x84ì\x86\x8cë\x85\x84ë\x8b¨) 'MIC Drop (Steve Aoki Remix)' Official MV", 'likes': 2454901}
{'title': "Marvel Studios' Avengers: Infinity War Official Trailer", 'likes': 2444956}


Top_10_Liked_Videos:  [{'title': "BTS (ë°©í\x83\x84ì\x86\x8cë\x85\x84ë\x8b¨) 'FAKE LOVE' Official MV", 'likes': 4924056}, {'title': "BTS (ë°©í\x83\x84ì\x86\x8cë\x85\x84ë\x8b¨) 'FAKE LOVE' Official MV", 'likes': 4750254}, {'title': "BTS (ë°©í\x83\x84ì\x86\x8cë\x85\x84ë\x8b¨) 'FAKE LOVE' Official MV", 'likes': 4470888}, {'title': "BTS (ë°©í\x83\x84ì\x86\x8cë\x85\x84ë\x8b¨) 'FAKE LOVE' Official MV", 'likes': 3880074}, {'title': 'YouTube Rewind: The Shape of 2017 | #YouTubeRewind', 'likes': 2811217}, {'title': 'YouTube Rewind: The Shape of 2017 | #YouTubeRewind', 'likes': 2656675}, {'title': "Marvel Studios' Avengers: Infinity War Official Trailer", 'likes': 2513103}, {'title': 'Childish Gambino - This Is America (Official Video)', 'likes': 2478908}, {'title': "BTS (ë°©í\x83\x84ì\x86\x8cë\x85\x84ë\x8b¨) 'MIC Drop (Steve Aoki Remix)' Official MV", 'likes': 2454901}, {'title': "Marvel Studios' Avengers: Infinity War Official Trailer", 'likes': 2444956}]     



{'title': 'YouTube Rewind: The Shape of 2017 | #YouTubeRewind', 'views': 113876217}
{'title': 'YouTube Rewind: The Shape of 2017 | #YouTubeRewind', 'views': 100911567}
{'title': "Marvel Studios' Avengers: Infinity War Official Trailer", 'views': 80360459}
{'title': 'YouTube Rewind: The Shape of 2017 | #YouTubeRewind', 'views': 75969469}
{'title': "Marvel Studios' Avengers: Infinity War Official Trailer", 'views': 74789251}
{'title': "BTS (ë°©í\x83\x84ì\x86\x8cë\x85\x84ë\x8b¨) 'FAKE LOVE' Official MV", 'views': 73463137}
{'title': 'Childish Gambino - This Is America (Official Video)', 'views': 73432600}
{'title': "Marvel Studios' Avengers: Infinity War Official Trailer", 'views': 66637636}
{'title': "BTS (ë°©í\x83\x84ì\x86\x8cë\x85\x84ë\x8b¨) 'FAKE LOVE' Official MV", 'views': 65396157}
{'title': "BTS (ë°©í\x83\x84ì\x86\x8cë\x85\x84ë\x8b¨) 'FAKE LOVE' Official MV", 'views': 62796390}

Top_10_Most_Viewed_Videos:  [{'title': 'YouTube Rewind: The Shape of 2017 | #YouTubeRewind', 'views': 113876217}, {'title': 'YouTube Rewind: The Shape of 2017 | #YouTubeRewind', 'views': 100911567}, {'title': "Marvel Studios' Avengers: Infinity War Official Trailer", 'views': 80360459}, {'title': 'YouTube Rewind: The Shape of 2017 | #YouTubeRewind', 'views': 75969469}, {'title': "Marvel Studios' Avengers: Infinity War Official Trailer", 'views': 74789251}, {'title': "BTS (ë°©í\x83\x84ì\x86\x8cë\x85\x84ë\x8b¨) 'FAKE LOVE' Official MV", 'views': 73463137}, {'title': 'Childish Gambino - This Is America (Official Video)', 'views': 73432600}, {'title': "Marvel Studios' Avengers: Infinity War Official Trailer", 'views': 66637636}, {'title': "BTS (ë°©í\x83\x84ì\x86\x8cë\x85\x84ë\x8b¨) 'FAKE LOVE' Official MV", 'views': 65396157}, {'title': "BTS (ë°©í\x83\x84ì\x86\x8cë\x85\x84ë\x8b¨) 'FAKE LOVE' Official MV", 'views': 62796390}]



correlation_between:  {'columns': ['views', 'likes', 'dislikes', 'comment_count'], 'index': ['views', 'likes', 'dislikes', 'comment_count'], 'data': [[1.0, 0.8241886774, 0.5560000663, 0.705515967], [0.8241886774, 1.0, 0.4602076798, 0.8524923709], [0.5560000663, 0.4602076798, 1.0, 0.6421435046], [0.705515967, 0.8524923709, 0.6421435046, 1.0]]}

'''

'''
jsondata = [
    
    {title     : 'Entertainment', likes: 9964},

    ]
'''

