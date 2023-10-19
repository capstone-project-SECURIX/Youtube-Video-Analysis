import requests
from bs4 import BeautifulSoup
import pandas as pd

def search_youtube(query, num_results=10):
    search_url = f"https://www.youtube.com/results?search_query={query}"
    response = requests.get(search_url)
    
    # Save the HTML content to a file
    with open("results.html", "w", encoding="utf-8") as html_file:
        html_file.write(response.text)
    
    soup = BeautifulSoup(response.text, "html.parser")

    video_data = []
    for item in soup.select(".yt-lockup-content"):
        video_title = item.select_one(".yt-lockup-title a").text.strip()
        video_views = item.select_one(".yt-lockup-meta-info li").text.strip()

        video_data.append({
            "Title": video_title,
            "Views": video_views,
        })

        if len(video_data) >= num_results:
            break

    return pd.DataFrame(video_data)

if __name__ == "__main__":
    query = "Python programming"
    num_results = 5
    
    search_results = search_youtube(query, num_results)
    print(search_results)

'''
https://www.youtube.com/results?search_query=Python
'''