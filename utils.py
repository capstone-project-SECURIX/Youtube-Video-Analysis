import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import re


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
    r"static/datasets/DEvideos.csv",
    r"static/datasets/INvideos.csv"
]

csvfilepath = file_paths[4]
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

def channel_video_all_details(df, channel_title):
    # Filter the DataFrame for videos by the specified channel_title
    channel_df = df[df['channel_title'] == channel_title]

    # Iterate through the filtered DataFrame and print video details
    for index, row in channel_df.iterrows():
        print("VideoID:", row['video_id'])
        print("Title:", row['title'])
        print("Views:", row['views'])
        print("Likes:", row['likes'])
        print("Dislikes:", row['dislikes'])
        print("CommentCount:", row['comment_count'])
        print("ThumbnailLink:", row['thumbnail_link'])
        print("CommentsDisabled:", row['comments_disabled'])
        print("RatingsDisabled:", row['ratings_disabled'])
        print("VideoErrororRemoved:", row['video_error_or_removed'])
        print("Description:", row['description'])
        print("\n")

def channel_summary(df, channel_title):
    # Filter the DataFrame for videos by the specified channel_title
    channel_df = df[df['channel_title'] == channel_title]

    # Calculate Total Views
    total_views = channel_df['views'].sum()

    # Calculate Average Views
    average_views = channel_df['views'].mean()

    # Calculate Total Likes
    total_likes = channel_df['likes'].sum()

    # Calculate Average Likes
    average_likes = channel_df['likes'].mean()

    # Calculate Total Dislikes
    total_dislikes = channel_df['dislikes'].sum()

    return {
        'TotalViews': total_views,
        'AverageViews': average_views,
        'TotalLikes': total_likes,
        'AverageLikes': average_likes,
        'TotalDislikes': total_dislikes
    }

def channel_summary_extended(df, channel_title):
    # Filter the DataFrame for videos by the specified channel_title
    channel_df = df[df['channel_title'] == channel_title]

    # Calculate Average Dislikes
    average_dislikes = channel_df['dislikes'].mean()

    # Calculate Total Comments
    total_comments = channel_df['comment_count'].sum()

    # Calculate Average Comments
    average_comments = channel_df['comment_count'].mean()

    # Find Most Liked Video
    most_liked_video = channel_df[channel_df['likes'] == channel_df['likes'].max()].iloc[0]

    # Find Most Disliked Video
    most_disliked_video = channel_df[channel_df['dislikes'] == channel_df['dislikes'].max()].iloc[0]

    return {
        'AverageDislikes': average_dislikes,
        'TotalComments': total_comments,
        'AverageComments': average_comments,
        'MostLikedVideo': {
            'VideoID': most_liked_video['video_id'],
            'Title': most_liked_video['title'],
            'thumbnail_link': most_liked_video['thumbnail_link'],
            'Likes': most_liked_video['likes'],
        },
        'MostDislikedVideo': {
            'Title': most_disliked_video['title'],
            'Dislikes': most_disliked_video['dislikes'],
            'VideoID': most_disliked_video['video_id'],
            'thumbnail_link': most_disliked_video['thumbnail_link'],

        }
    }

def channel_summary_extended_v2(df, channel_title):
    # Filter the DataFrame for videos by the specified channel_title
    channel_df = df[df['channel_title'] == channel_title]

    # Video with Most Comments
    most_commented_video = channel_df[channel_df['comment_count'] == channel_df['comment_count'].max()].iloc[0]

    # Channel Engagement
    total_likes = channel_df['likes'].sum()
    total_dislikes = channel_df['dislikes'].sum()
    total_comments = channel_df['comment_count'].sum()
    total_views = channel_df['views'].sum()
    channel_engagement = {
        'TotalLikes': total_likes,
        'TotalDislikes': total_dislikes,
        'TotalComments': total_comments,
        'TotalViews': total_views,
        'EngagementRate': {
            'LikesperView': total_likes / total_views,
            'DislikesperView': total_dislikes / total_views,
            'CommentsperView': total_comments / total_views
        }
    }

    # Popular Thumbnail Colors (placeholder code)
    thumbnail_colors = ['Red', 'Blue', 'Green']  # Analyze your data for this metric

    # Time Analysis (assuming 'publish_time' is a timestamp column)
    # channel_df['publish_time'] = pd.to_datetime(channel_df['publish_time'])
    # channel_df['publish_hour'] = channel_df['publish_time'].dt.hour
    # publish_time_counts = channel_df['publish_hour'].value_counts()

    # Time Analysis (assuming 'publish_time' is a timestamp column)
    channel_df['publish_time'] = pd.to_datetime(channel_df['publish_time'])
    channel_df['publish_hour'] = channel_df['publish_time'].dt.hour
    TimeAnalysis  = channel_df['publish_hour'].value_counts().sort_index().tolist()

    # Ensure publish_time_counts has data for all 24 hours
    publish_time_counts = np.zeros(24)


    # Update publish_time_counts based on the available data
    for hour, count in enumerate(TimeAnalysis ):
        publish_time_counts[hour] = count

    # Create a line chart
    plt.plot(range(24), publish_time_counts, marker='o')
    plt.title('Time Analysis')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Count')
    plt.grid(True)

    # Save the chart as an image
    plt.savefig('static/tempimgs/time_analysis.png')

    # Day of the Week Analysis
    # channel_df['publish_day'] = channel_df['publish_time'].dt.day_name()
    # publish_day_counts = channel_df['publish_day'].value_counts()

    # Day of the Week Analysis
    channel_df['publish_day'] = channel_df['publish_time'].dt.day_name()
    publish_day_counts = channel_df['publish_day'].value_counts().to_dict()

    # Extract days and counts from publish_day_counts
    days = list(publish_day_counts.keys())
    counts = [publish_day_counts[day] for day in days]

    # Create a bar chart
    plt.bar(days, counts)
    plt.title('Day of the Week Analysis')
    plt.xlabel('Day')
    plt.ylabel('Count')

    # Save the chart as an image
    plt.savefig('static/tempimgs/day_of_week_analysis.png')


    return {
        'VideowithMostComments': {
            'Title': most_commented_video['title'],
            'Comments': most_commented_video['comment_count'],
            'VideoID': most_commented_video['video_id'],
            'thumbnail_link': most_commented_video['thumbnail_link'],

        },
        'ChannelEngagement': channel_engagement,
        'PopularThumbnailColors': thumbnail_colors,
        'TimeAnalysis': TimeAnalysis ,
        'DayoftheWeekAnalysis': publish_day_counts
    }

def clean_description(description_text):
    # Remove URLs
    description_text = re.sub(r'http\S+', '', description_text)
    description_text = re.sub(r'www\S+', '', description_text)

    # Remove newline characters
    description_text = description_text.replace('\n', ' ')
    description_text = description_text.replace('\\n', ' ')
    description_text = description_text.replace('|', ' ')
    description_text = description_text.replace('#', ' ')
    description_text = description_text.replace('-', ' ')
    description_text = description_text.replace('.', ' ')
    description_text = description_text.replace(',', ' ')
    description_text = description_text.replace(';', ' ')
    description_text = description_text.replace("'", ' ')
    description_text = description_text.replace('(', ' ')
    description_text = description_text.replace(')', ' ')
    description_text = description_text.replace('Subscribe:', ' ')
    description_text = description_text.replace('Like:', ' ')
    description_text = description_text.replace('Follow:', ' ')
    description_text = description_text.replace('etc', ' ')
    description_text = description_text.replace('\t', ' ')

    return description_text

def channel_summary_analysis(df, channel_title):
    # Filter the DataFrame for videos by the specified channel_title
    channel_df = df[df['channel_title'] == channel_title]

    # Top Keywords in Titles
    all_keywords = ' '.join(channel_df['title'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_keywords)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Top Keywords in Titles")
    plt.savefig('static/tempimgs/top_keywords_wordcloud.png')  # Save the word cloud image
    plt.close()  # Close the plot



    # Channel Interaction: Analyze the relationship between likes, dislikes, and comments
    channel_df['interaction_rate'] = (channel_df['likes'] + channel_df['dislikes']) / channel_df['comment_count']
    
    # # Video Length Analysis: Study the relationship between video length and views
    # channel_df['video_duration'] = pd.to_numeric(channel_df['video_duration'], errors='coerce')
    # video_length_vs_views = channel_df.groupby('video_duration')['views'].mean()
    
    # Top Viewed Categories: Identify the most viewed video categories
    top_categories = channel_df['category_id'].value_counts().nlargest(5)
    top_categories = top_categories.index.tolist()

    # Word Cloud Analysis: Create word clouds from video descriptions
    all_descriptions = ' '.join(channel_df['description'])
    all_descriptionsword = clean_description(all_descriptions)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_descriptionsword)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Word Cloud Analysis of Video Descriptions")
    plt.savefig('static/tempimgs/description_wordcloud.png')  # Save the word cloud image
    plt.close()  # Close the plot


    return {
        "TopKeywordsinTitles": all_keywords,
        "ChannelInteraction": channel_df['interaction_rate'].mean(),
        # "Video Length vs Views": video_length_vs_views.to_dict(),
        "TopViewedCategories": top_categories,
        "WordCloudAnalysis": all_descriptions
    }



# Example usage:
# Replace 'df' with your actual DataFrame, and 'channel_title' with the channel name


# print("Top_5_Categories_with_Most_Videos: ",Top_5_Categories_with_Most_Videos(df))
# print("\n\n")
# print("Top_10_Liked_Videos: ",Top_10_Liked_Videos(df))
# print("\n\n")

# print("Top_10_Most_Viewed_Videos: ",Top_10_Most_Viewed_Videos(df))
# print("\n\n")

# print("correlation_between: ",correlation_between(df))

# test - 2

# channel_title = "EminemVEVO" 
# channel_title = "Saregama TVShows" 
channel_title = "Top Telugu TV" # IN-dataset 

# print(channel_Top_10_Liked_Videos(df, channel_title))
# print(channel_Top_Viewed_Video(df, channel_title))
# print(channel_Top_Impression_Video(df, channel_title))
# print(channel_video_all_details(df, channel_title))

# print(channel_summary(df, channel_title))
# print(channel_summary_extended(df, channel_title))
# print(channel_summary_extended_v2(df, channel_title))
# print(channel_summary_analysis(df, channel_title))

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

'''
video_id,trending_date,title,channel_title,category_id,publish_time,tags,views,likes,dislikes,comment_count,thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description


EJVvdjDGnak,17.14.11,Nagarjuna Funny Comments on Samantha Dress || Naga Chaitany Samantha Akkineni Wedding Reception 2017,Top Telugu TV,24,2017-11-13T07:26:33.000Z,"Nagarjuna Funny Comments on Samantha Dress|""Naga Chaitany Samantha Akkineni Wedding Reception 2017""|""nagarjuna shocking comments on samantha dress""|""nagarjuna funny comments""|""samantha dress""|""samantha wedding reception""|""samantha""|""dress""|""nagarjuna""|""funny""|""naga chaitany""|""naga chaitany samantha""|""samantha wedding""|""#chaisam""|""akkineni reception live""|""grand reception for #chaysam""|""samantha akkineni""|""naga chaitanya""|""akkineni naga chaitanya""|""samantha marriage video""",256199,318,123,35,https://i.ytimg.com/vi/EJVvdjDGnak/default.jpg,FALSE,FALSE,FALSE,"This video about Nagarjuna Funny Comments on Samantha Dress || Naga Chaitany Samantha Akkineni Wedding Reception 2017 and also The Naga Chaitanya - Samantha Ruth Prabhu wedding festivities just won't slow down! After two weddings and a reception, the family of the newlyweds have arranged for another starry reception for the couple, this time in Hyderabad. So there we have Naga Chaitanya looking quite dashing in that navy blue suit. But it is Samantha Ruth Prabhu's outfit of the night that won't allow us to take our eyes off her! Dressed in a gorgeous silvery white gown with a bluish hue, Samantha looked like a beautiful painting come alive, and we have to say Mr Chaitanya is one lucky guy. \nTalking about the reception, it was one star-studded affair as expected. Among the prominent celebs who came to the reception and gave the newlyweds their wishes and blessing, were Megastar Chiranjeevi and his family, including Ram Charan, Allu Arjun and Varun Tej. Baahubali director SS Rajamouli was a guest as well. He had directed Samantha in the fantasy thriller, Ee (Makkhi in Hindi). Then there was Venkatesh, looking quite suave in that suit. Other celebs were present were Vamshi Paidipally, Nandamuri Harikrishna, UV Krishnam Raju, Krishna, Murali Mohan, Nikhil Siddharth, Nani, Rakul Preet and Rashi Khanna. Rana Daggubati, who is also Naga Chaitanya's cousin, was also there to be with the family.\n\n\nSubscribe: https://www.youtube.com/channel/UC8Dj-LDol8r7zGnhn0onF0A\nLike: https://www.facebook.com/TopTeluguTV/\nFollow: https://twitter.com/TopTeluguTV/"




Video ID: 7lgpLbn6RnM
Title: Naga Babu Fun on Allu Arjun Dance in LOVER ALSO FIGHTER ALSO Song | Naa Peru Surya Pre Release
Views: 358511
Likes: 2976
Dislikes: 204
Comment Count: 187
Thumbnail Link: https://i.ytimg.com/vi/7lgpLbn6RnM/default.jpg
Comments Disabled: False
Ratings Disabled: False
Video Error or Removed: False
Description: Naga Babu Fun on Allu Arjun Dance in LOVER ALSO FIGHTER ALSO Song | Naa Peru Surya Naa Illu India Pre Release Event | Top Telugu TV#NaaPeruSuryaNaaIlluIndia 2018 Telugu movie ft. Allu Arjun and Anu Emmanuel. Music By Vishal - Shekhar. Directed By Vakkantham Vamsi and Produced By Sirisha Sridhar Lagadapati & Bunny Vas under Ramalakshmi Cine Creations. Presented by Naga Babu.Top Telugu TV is the first Channel which Concentrates Only on Youth Life Style, Education, Health Tips, Achievements, Events, Entertainment, Movie Promotions etc..https://www.toptelugutv.comLike: https://www.facebook.com/toptelugutvchannel/Follow: https://twitter.com/TopTeluguTV/Subscribe: https://www.youtube.com/channel/UC8Dj-LDol8r7zGnhn0onF0Ahttps://www.instagram.com/toptelugutv/?hl=en

'''