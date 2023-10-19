import re
import json

# Load HTML content
with open('results.html') as f:
    html = f.read()

# print(html)

# # Extract initial data JSON
# match = re.search(r'var ytInitialData = {.*};    </script>', html)
# print(match)

# title: {
# simpleText:
# "Python 9 Hours Full Course From Scratch | Intellipaat",
# }

# Sample HTML content
# html = """

# videoRenderer: {
# videoId: "vLqTf2b6GZw",


#   thumbnails: [
#     {
#       url: "https://i.ytimg.com/vi/vLqTf2b6GZw/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=\u0026rs=AOn4CLCw6U0CXIC_iBaiwLaTq8SsD0L_fw",
#       width: 360,
#       height: 202,
#     },

# accessibilityData: {
#     label: "1 hour, 17 minutes, 12 seconds",
# },

# viewCountText: { simpleText: "7,735,601 views" },


# description: {
# simpleText:
# "Learn Python from basics to advanced",
# },
# """



# Pattern for extracting
title_pattern = r'title: {\s*simpleText:\s*"([^"]*)",\s*}'
description_pattern = r'description: {\s*simpleText:\s*"([^"]*)",\s*}'

# Find all title matches in the HTML content
title_matches = re.finditer(title_pattern, html)

# Find all description matches in the HTML content
description_matches = re.finditer(description_pattern, html)

# Extract and print all titles
for match in description_matches:
    title = match.group(1)
    print("description_matches:", title)

# # Extract and print all title and description texts
# for title_match, description_match in zip(title_matches, description_matches):
#     title = title_match.group(1)
#     description = description_match.group(1)
#     print("Title:", title)
#     print("Description:", description)
#     print()


# print(match.group())



# data = json.loads(match.group(1))
# print(data)

# # Get video data 
# video_data = data['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['searchPyvRenderer']['ads'][0]['adSlotRenderer']['fulfillmentContent']['fulfilledLayout']['inFeedAdLayoutRenderer']['renderingContent']['promotedVideoRenderer']

# # Extract fields
# video_id = video_data['videoId']
# title = video_data['title']['simpleText']
# description = video_data['description']['simpleText']  
# thumbnails = [thumb['url'] for thumb in video_data['thumbnail']['thumbnails']]
# channel = video_data['longBylineText']['runs'][0]['text']
# length = video_data['lengthText']['simpleText']
# views = video_data['viewCountText']['simpleText']

# # Print video details
# print('Video ID:', video_id)
# print('Title:', title) 
# print('Description:', description)
# print('Thumbnails:', thumbnails)
# print('Channel:', channel)
# print('Length:', length)
# print('Views:', views)

# ----------------------------------

# # Define the regular expression pattern
# pattern = r'var ytInitialData = {'

# # Search for the pattern in the HTML content
# match = re.search(pattern, html)

# # Check if a match is found
# if match:
#     print("Match found at position:", match.start())
# else:
#     print("Match not found.")