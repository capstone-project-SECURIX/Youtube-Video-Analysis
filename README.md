# Youtube-Video-Analysis BDA (Subject Project) : Youtube-Video-Analysis

**person vise analysis : channel_title**
- top liked videos list
- top viewed video
- top impression (for impression use likes and dislikes and views)

**Datasets:**
- [USvideos](static/datasets/USvideos.csv)
- [RUvideos](static/datasets/RUvideos.csv)
- [CAvideos](static/datasets/CAvideos.csv)
- [DEvideos](static/datasets/DEvideos.csv)
- [INvideos](static/datasets/INvideos.csv)

**Dataset Link:** [Kaggle - YouTube New](https://www.kaggle.com/datasets/datasnaek/youtube-new)

**UPDATE:** Source code used for collecting this data [released here](https://www.kaggle.com/datasnaek/youtube)

## Context
YouTube (the world-famous video-sharing website) maintains a list of the top trending videos on the platform. To determine the year's top-trending videos, YouTube uses a combination of factors, including measuring users' interactions (number of views, shares, comments, and likes). Note that they're not the most-viewed videos overall for the calendar year. Top performers on the YouTube trending list are music videos, celebrity and/or reality TV performances, and the random dude-with-a-camera viral videos that YouTube is well-known for. This dataset is a daily record of the top trending YouTube videos.

## Content
This dataset includes several months (and counting) of data on daily trending YouTube videos. Data is included for the US, GB, DE, CA, and FR regions (USA, Great Britain, Germany, Canada, and France, respectively), with up to 200 listed trending videos per day. Now includes data from RU, MX, KR, JP, and IN regions (Russia, Mexico, South Korea, Japan, and India, respectively) over the same time period. Each region's data is in a separate file. Data includes the video title, channel title, publish time, tags, views, likes and dislikes, description, and comment count. The data also includes a `category_id` field, which varies between regions. To retrieve the categories for a specific video, find it in the associated JSON. One such file is included for each of the five regions in the dataset.

For more information on specific columns in the dataset, refer to the [column metadata](https://www.kaggle.com/datasnaek/youtube-new).

## Acknowledgements
This dataset was collected using the YouTube API.

## Inspiration
Possible uses for this dataset could include:

- Sentiment analysis in a variety of forms
- Categorizing YouTube videos based on their comments and statistics.
- Training ML algorithms like RNNs to generate their own YouTube comments.
- Analyzing what factors affect how popular a YouTube video will be.
- Statistical analysis over time.

For further inspiration, see the [kernels on this dataset](https://www.kaggle.com/datasnaek/youtube-new/kernels).

```R
# Load the CSV file into a data frame
csv_file_path <- 'static/datasets/USvideos.csv'
df <- read.csv(csv_file_path, encoding = 'latin1')

# Define a category mapping as a named character vector
category_mapping <- c(
  "1" = 'Film & Animation',
  "2" = 'Autos & Vehicles',
  # ... (category mappings for other category IDs)
  "44" = 'Trailers'
)

# Function to get the top 5 categories with the most videos
top_5_categories <- function(df) {
  # Ensure the "category_id" column exists in your data
  if ("category_id" %in% colnames(df)) {
    # Get the top 5 categories and their counts
    top_categories <- as.data.frame(table(df$category_id))
    
    # Map category IDs to names
    top_categories$category_id <- sapply(top_categories$category_id, function(cat_id) category_mapping[as.character(cat_id)])
    
    # Rename columns
    colnames(top_categories) <- c("Category", "Count")
    
    # Convert to a list
    jsondata <- as.list(top_categories)
    return(jsondata)
  } else {
    return("The 'category_id' column is not found in the dataset.")
  }
}

Top_10_Liked_Videos <- function(df) {
  # Sort the DataFrame by 'likes' in descending order and select the top 10 rows
  top_rated_videos <- head(arrange(df, desc(likes)), 10)

  # Extract the video titles and likes
  video_titles <- top_rated_videos$title
  video_likes <- top_rated_videos$likes

  # Create a list of video information
  video_info_list <- lapply(1:10, function(i) {
    list(title = video_titles[i], likes = video_likes[i])
  })

  # Convert the list to a JSON-like structure
  jsondata <- lapply(video_info_list, toJSON, pretty = TRUE)

  # Print the resulting JSON-like data
  for (item in jsondata) {
    cat(item, "\n")
  }

  return(jsondata)
}

Top_10_Most_Viewed_Videos <- function(df) {
  # Sort the DataFrame by 'views' in descending order and select the top 10 rows
  top_viewed_videos <- head(arrange(df, desc(views)), 10)

  # Extract the video titles and views
  video_titles <- top_viewed_videos$title
  video_views <- top_viewed_videos$views

  # Create a list of video information
  video_info_list <- lapply(1:10, function(i) {
    list(title = video_titles[i], views = video_views[i])
  })

  # Convert the list to a JSON-like structure
  jsondata <- lapply(video_info_list, toJSON, pretty = TRUE)

  # Print the resulting JSON-like data
  for (item in jsondata) {
    cat(item, "\n")
  }

  return(jsondata)
}


correlation_between <- function(df) {
  # Select the columns for which you want to calculate correlations
  selected_columns <- df[c('views', 'likes', 'dislikes', 'comment_count')]
  
  # Calculate the correlation matrix
  correlation_matrix <- cor(selected_columns, use = 'pairwise.complete.obs')
  
  # Convert the correlation matrix to a list
  correlation_data <- as.list(correlation_matrix)
  
  return(correlation_data)
}

# -------------------------------------------------------------------

channel_Top_10_Liked_Videos <- function(df, channel_title) {
  # Filter the DataFrame for videos by the specified channel_title
  channel_df <- df[df$channel_title == channel_title, ]
  
  # Get the top 10 most liked videos from the filtered DataFrame
  top_liked_videos <- head(arrange(channel_df, desc(likes)), 10)
  
  # Extract the desired columns
  top_liked_videos <- top_liked_videos[c('video_id', 'title', 'likes', 'views', 'thumbnail_link')]
  
  # Convert the top 10 liked videos to a list of dictionaries (data frames)
  top_liked_videos_list <- as.data.frame(top_liked_videos)
  
  return(top_liked_videos_list)
}

channel_Top_Viewed_Video <- function(df, channel_title) {
  # Filter the DataFrame for videos by the specified channel_title
  channel_df <- df[df$channel_title == channel_title, ]
  
  # Find the video with the highest views from the filtered DataFrame
  top_viewed_video <- channel_df[which.max(channel_df$views), ]
  
  # Extract the desired columns
  top_viewed_video <- top_viewed_video[c('video_id', 'title', 'views', 'thumbnail_link')]
  
  # Convert the top viewed video to a list of dictionaries (data frames)
  top_viewed_video_list <- as.data.frame(top_viewed_video)
  
  return(top_viewed_video_list[1, ])  # Return the first (and only) row
}

channel_Top_Impression_Video <- function(df, channel_title) {
  # Filter the DataFrame for videos by the specified channel_title
  channel_df <- df[df$channel_title == channel_title, ]
  
  # Calculate an "impression" score for each video based on likes, dislikes, and views
  channel_df$impression <- (channel_df$likes - channel_df$dislikes) / channel_df$views
  
  # Find the video with the highest impression score from the filtered DataFrame
  top_impression_video <- channel_df[which.max(channel_df$impression), ]
  
  # Extract the desired columns
  top_impression_video <- top_impression_video[c('video_id', 'title', 'impression', 'thumbnail_link')]
  
  # Convert the top impression video to a list of dictionaries (data frames)
  top_impression_video_list <- as.data.frame(top_impression_video)
  
  return(top_impression_video_list[1, ])  # Return the first (and only) row
}

```
# ... (R functions for other analysis tasks)



# Example usage of the functions

# Load the dataset
    csv_file_path <- 'static/datasets/USvideos.csv'
    df <- read.csv(csv_file_path, encoding = 'latin1')

# Use the functions to analyze the data
    result <- top_5_categories(df)
    result <- Top_10_Liked_Videos(df)
    result <- Top_10_Most_Viewed_Videos(df)
    result <- correlation_between(df)

# Channel-specific analysis
    result <- channel_Top_10_Liked_Videos(df, "CaseyNeistat")
    result <- channel_Top_Viewed_Video(df, "CaseyNeistat")
    result <- channel_Top_Impression_Video(df, "CaseyNeistat")

# Print the results, or you can save them to a file or display in your web application
    print(result)

# Have fun analyzing your YouTube video data!

## File Structure

Your Flask app is organized with a well-structured file hierarchy for easy maintenance and readability.

### Root Directory

    - `analyze_youtube_data.r`: This file contains R language code for analyzing YouTube datasets, including functions for top categories, top liked videos, top viewed videos, and correlation analysis.

    - `app.py`: This is the main Python file for your Flask application. It defines your application routes, views, and handles the communication between the back end and front end.

    - `install.r`: This script likely contains instructions or commands for installing necessary packages or dependencies required for your R scripts.

    - `utils.py`: This Python file contains all the functions necessary for the analysis of your YouTube datasets. It provides functions like `top_5_categories`, `Top_10_Liked_Videos`, `Top_10_Most_Viewed_Videos`, and `correlation_between`. These functions are used in your Flask app to serve data to the front end.

### Static Directory

    - `datasets`: This folder is where your YouTube dataset files are stored. You have various country-specific datasets in this directory. These datasets serve as the source for your analysis.

    - `tempimgs`: This directory likely stores temporary images generated during the analysis or visualization of your data.

    - `tailwindcss.js`: This JavaScript file might be related to the use of Tailwind CSS in your project. Tailwind CSS is a utility-first CSS framework.

### Templates Directory

    - `base.html`: This is the base HTML template that serves as the common structure for other HTML templates. It typically contains the layout and structure shared across multiple pages.

    - `channelData.html`: This HTML template might be used to display data specific to a YouTube channel, such as top-liked videos, top-viewed video, and top impression video.

    - `index.html`: This HTML template likely displays data for the entire dataset at a country level. It may include data summaries like top categories, top-liked videos, top-viewed videos, and correlation analyses.

    - `rlang.html`: This HTML template appears to be dedicated to displaying R language code for both country datasets and channel-specific data analysis.

### YouTube-Dataset Directory

    - This directory is named after your YouTube datasets, and it appears to contain the full dataset files.

### Miscellaneous

You may have other files or directories specific to your Flask app's functionality and organization.

The described file structure demonstrates a clean separation of concerns between your R data analysis scripts, Python Flask app, and static assets like datasets and templates. This structure makes it easier to maintain and scale your YouTube video analysis application.
