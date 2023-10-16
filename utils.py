import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns



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

csvfilepath = file_paths[2]
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

    # Create bar chart
    categories = [item['cat'] for item in jsondata]
    counts = [item['count'] for item in jsondata]

    plt.figure(figsize=(10, 6))  # Adjust the figure size
    plt.bar(categories, counts)
    plt.xlabel('Categories')
    plt.ylabel('Number of Videos')
    plt.title('Top 5 Categories with Most Videos')
    
    # Save the image in the static/tempimgs folder
    plt.savefig('static/tempimgs/top_categories_bar_chart.png')

    return jsondata

def Top_10_Liked_Videos(df):
    top_rated_videos = df.nlargest(10, 'likes')

    jsondata = []

    for index, row in top_rated_videos.iterrows():
        video_info = {'title': row['title'], 'likes': row['likes']}
        jsondata.append(video_info)

    # Create a line chart for the top 10 liked videos
    video_titles = [item['title'] for item in jsondata]
    video_likes = [item['likes'] for item in jsondata]

    plt.figure(figsize=(10, 6))  # Adjust the figure size
    plt.plot(video_titles, video_likes, marker='o', linestyle='-')
    plt.xlabel('Video Titles')
    plt.ylabel('Number of Likes')
    plt.title('Top 10 Liked Videos')

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=90)
    plt.tight_layout()  # Ensure labels are not cut off

    # Save the image in the static/tempimgs folder
    plt.savefig('static/tempimgs/top_liked_videos_line_chart.png')

    # Print the resulting JSON data
    for item in jsondata:
        print(item)

    return jsondata

def Top_10_Most_Viewed_Videos(df):
    top_viewed_videos = df.nlargest(10, 'views')

    jsondata = []

    for index, row in top_viewed_videos.iterrows():
        video_info = {'title': row['title'], 'views': row['views']}
        jsondata.append(video_info)

    # Create a bar chart for the top 10 most viewed videos
    video_titles = [item['title'] for item in jsondata]
    video_views = [item['views'] for item in jsondata]

    plt.figure(figsize=(10, 6))  # Adjust the figure size
    plt.bar(video_titles, video_views)
    plt.xlabel('Video Titles')
    plt.ylabel('Number of Views')
    plt.title('Top 10 Most Viewed Videos')

    # Save the image in the static/tempimgs folder
    plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility
    plt.tight_layout()  # Ensure labels are not cut off
    plt.savefig('static/tempimgs/top_viewed_videos_bar_chart.png')

    # Print the resulting JSON data
    for item in jsondata:
        print(item)

    return jsondata

def correlation_between(df):
    # Calculate the correlation matrix
    correlation_matrix = df[['views', 'likes', 'dislikes', 'comment_count']].corr()

    # Convert the correlation matrix to a JSON string
    correlation_json = correlation_matrix.to_json(orient='split')

    # Now, parse the JSON string to a Python dictionary
    correlation_data = json.loads(correlation_json)

    # Create a heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')

    # Save the image in the static/tempimgs folder
    plt.tight_layout()
    plt.savefig('static/tempimgs/correlation_heatmap.png')

    return correlation_data

# ------- new ------------------

def channel_Top_10_Liked_Videos(df, channel_title):
    # Filter the DataFrame for videos by the specified channel_title
    channel_df = df[df['channel_title'] == channel_title]
    
    # Get the top 10 most liked videos from the filtered DataFrame
    top_liked_videos = channel_df.nlargest(10, 'likes')
    
    # Extract the desired columns
    top_liked_videos = top_liked_videos[['video_id', 'title', 'likes', 'views', 'thumbnail_link']]
    
    # Convert the top 10 liked videos to a list of dictionaries
    top_liked_videos_list = top_liked_videos.to_dict(orient='records')
    
    return top_liked_videos_list

def channel_Top_Viewed_Video(df, channel_title):
    # Filter the DataFrame for videos by the specified channel_title
    channel_df = df[df['channel_title'] == channel_title]
    
    # Find the video with the highest views from the filtered DataFrame
    top_viewed_video = channel_df.nlargest(1, 'views')
    
    # Extract the desired columns
    top_viewed_video = top_viewed_video[['video_id', 'title', 'views', 'thumbnail_link']]
    
    return top_viewed_video.to_dict(orient='records')[0]

def channel_Top_Impression_Video(df, channel_title):
    # Filter the DataFrame for videos by the specified channel_title
    channel_df = df[df['channel_title'] == channel_title].copy()
    
    # Calculate an "impression" score for each video based on likes, dislikes, and views
    channel_df['impression'] = ((channel_df['likes'] - channel_df['dislikes']) / channel_df['views'] * 100)
    
    # Find the video with the highest impression score from the filtered DataFrame
    top_impression_video = channel_df.nlargest(1, 'impression')
    
    # Extract the desired columns
    top_impression_video = top_impression_video[['video_id', 'title', 'impression', 'thumbnail_link']]
    
    return top_impression_video.to_dict(orient='records')[0]

def channel_Total_Videos(df, channel_title):
    # Filter the DataFrame for videos by the specified channel_title
    channel_df = df[df['channel_title'] == channel_title]
    
    # Get the total number of videos for the channel
    total_videos = len(channel_df)
    
    return total_videos



# print("Top_5_Categories_with_Most_Videos: ",Top_5_Categories_with_Most_Videos(df))
# print("\n\n")
# print("Top_10_Liked_Videos: ",Top_10_Liked_Videos(df))
# print("\n\n")

# print("Top_10_Most_Viewed_Videos: ",Top_10_Most_Viewed_Videos(df))
# print("\n\n")

# print("correlation_between: ",correlation_between(df))

# test - 2

# channel_title = "EminemVEVO" 
channel_title = "Saregama TVShows" 

# print(channel_Top_10_Liked_Videos(df, channel_title))
# print(channel_Top_Viewed_Video(df, channel_title))
# print(channel_Top_Impression_Video(df, channel_title))
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





print(channel_Top_10_Liked_Videos(df, channel_title))

[
    {'video_id': 'wfWIs2gFTAM', 'title': 'Eminem - River ft. Ed Sheeran', 'likes': 1013533, 'views': 20324769, 'thumbnail_link': 'https://i.ytimg.com/vi/wfWIs2gFTAM/default.jpg'}, 

    {'video_id': 'wfWIs2gFTAM', 'title': 'Eminem - River ft. Ed Sheeran', 'likes': 948050, 'views': 17403821, 'thumbnail_link': 'https://i.ytimg.com/vi/wfWIs2gFTAM/default.jpg'}, 
    
    {'video_id': 'n1WpP7iowLc', 'title': 'Eminem - Walk On Water (Audio) ft. BeyoncÃ©', 'likes': 891283, 'views': 24578152, 'thumbnail_link': 'https://i.ytimg.com/vi/n1WpP7iowLc/default.jpg'}, 
    
    {'video_id': 'wfWIs2gFTAM', 'title': 'Eminem - River ft. Ed Sheeran', 'likes': 869985, 'views': 14624941, 'thumbnail_link': 'https://i.ytimg.com/vi/wfWIs2gFTAM/default.jpg'}, {'video_id': 'n1WpP7iowLc', 'title': 'Eminem - Walk On Water (Audio) ft. BeyoncÃ©', 'likes': 869304, 'views': 22702386, 'thumbnail_link': 'https://i.ytimg.com/vi/n1WpP7iowLc/default.jpg'}, {'video_id': 'n1WpP7iowLc', 'title': 'Eminem - Walk On Water (Audio) ft. BeyoncÃ©', 'likes': 840642, 'views': 20539417, 'thumbnail_link': 'https://i.ytimg.com/vi/n1WpP7iowLc/default.jpg'}, {'video_id': 'n1WpP7iowLc', 'title': 'Eminem - Walk On Water (Audio) ft. BeyoncÃ©', 'likes': 787425, 'views': 17158579, 'thumbnail_link': 'https://i.ytimg.com/vi/n1WpP7iowLc/default.jpg'}, {'video_id': 'wfWIs2gFTAM', 'title': 'Eminem - River ft. Ed Sheeran', 'likes': 780459, 'views': 11939132, 'thumbnail_link': 'https://i.ytimg.com/vi/wfWIs2gFTAM/default.jpg'}, {'video_id': '3BXDsVD6O10', 'title': 'Eminem - River (Audio) ft. Ed Sheeran', 'likes': 755912, 'views': 18250437, 'thumbnail_link': 'https://i.ytimg.com/vi/3BXDsVD6O10/default.jpg'}, {'video_id': '3BXDsVD6O10', 'title': 'Eminem - River (Audio) ft. Ed Sheeran', 'likes': 708491, 'views': 15761943, 'thumbnail_link': 'https://i.ytimg.com/vi/3BXDsVD6O10/default.jpg'}]


print(channel_Top_Viewed_Video(df, channel_title))
    {'video_id': 'n1WpP7iowLc', 'title': 'Eminem - Walk On Water (Audio) ft. BeyoncÃ©', 'views': 24578152, 'thumbnail_link': 'https://i.ytimg.com/vi/n1WpP7iowLc/default.jpg'}

print(channel_Top_Impression_Video(df, channel_title))
    {'video_id': 'ryr75N0nki0', 'title': 'Eminem - Walk On Water (Official Video) ft. BeyoncÃ©', 'impression': 0.233165657041334, 'thumbnail_link': 'https://i.ytimg.com/vi/ryr75N0nki0/default.jpg'}

'''

'''
jsondata = [
    
    {title     : 'Entertainment', likes: 9964},

    ]
'''

