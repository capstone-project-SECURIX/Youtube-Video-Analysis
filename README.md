# Youtube-Video-Analysis
BDA (Subject Project) : Youtube-Video-Analysis


video_id,
trending_date,
title,
channel_title,
category_id,
publish_time,
tags,
views,
likes,
dislikes,
comment_count,
thumbnail_link,
comments_disabled,
ratings_disabled,
video_error_or_removed,
description

thumbnail_link, video_id



video_id,trending_date,title,channel_title,category_id,publish_time,tags,views,likes,dislikes,comment_count,thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description


n1WpP7iowLc,17.14.11,"Eminem - Walk On Water (Audio) ft. Beyoncé","EminemVEVO",10,2017-11-10T17:00:03.000Z,"Eminem"|"Walk"|"On"|"Water"|"Aftermath/Shady/Interscope"|"Rap",17158579,787425,43420,125882,https://i.ytimg.com/vi/n1WpP7iowLc/default.jpg,False,False,False,"Eminem's new track Walk on Water ft. Beyoncé is available everywhere: http://shady.sr/WOWEminem \nPlaylist Best of Eminem: https://goo.gl/AquNpo\nSubscribe for more: https://goo.gl/DxCrDV\n\nFor more visit: \nhttp://eminem.com\nhttp://facebook.com/eminem\nhttp://twitter.com/eminem\nhttp://instagram.com/eminem\nhttp://eminem.tumblr.com\nhttp://shadyrecords.com\nhttp://facebook.com/shadyrecords\nhttp://twitter.com/shadyrecords\nhttp://instagram.com/shadyrecords\nhttp://trustshady.tumblr.com\n\nMusic video by Eminem performing Walk On Water. (C) 2017 Aftermath Records\nhttp://vevo.ly/gA7xKt"


person vise analysis : channel_title
- top liked videos list
- top viewed video 
- top impression ( for impression use likes and dislikes and views)


give python function for it 

example:
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