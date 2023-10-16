# # Replace 'train.csv' with the actual path to your CSV file
# # csv_file_path <- 'train.csv'

# csv_file_path <- 'static/datasets/USvideos.csv'


# # Load the CSV file into a data frame
# df <- read.csv(csv_file_path)

# # Now you can work with the data frame 'df'
# head(df)  # Display the first few rows of the data frame
    

csv_file_path <- 'static/datasets/USvideos.csv'

# Load the CSV file into a data frame
df <- read.csv(csv_file_path, encoding = 'latin1')

# Print the first few rows of the data frame to verify its contents
# head(df)
library(dplyr)
library(jsonlite)



# Define a category mapping as a named character vector
category_mapping <- c(
  "1" = 'Film & Animation',
  "2" = 'Autos & Vehicles',
  "10" = 'Music',
  "15" = 'Pets & Animals',
  "17" = 'Sports',
  "18" = 'Short Movies',
  "19" = 'Travel & Events',
  "20" = 'Gaming',
  "21" = 'Videoblogging',
  "22" = 'People & Blogs',
  "23" = 'Comedy',
  "24" = 'Entertainment',
  "25" = 'News & Politics',
  "26" = 'Howto & Style',
  "27" = 'Education',
  "28" = 'Science & Technology',
  "29" = 'Nonprofits & Activism',
  "30" = 'Movies',
  "31" = 'Anime/Animation',
  "32" = 'Action/Adventure',
  "33" = 'Classics',
  "34" = 'Comedy',
  "35" = 'Documentary',
  "36" = 'Drama',
  "37" = 'Family',
  "38" = 'Foreign',
  "39" = 'Horror',
  "40" = 'Sci-Fi/Fantasy',
  "41" = 'Thriller',
  "42" = 'Shorts',
  "43" = 'Shows',
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


# Example usage of the functions

# result <- top_5_categories(df)
# result <- Top_10_Liked_Videos(df)
# result <- Top_10_Most_Viewed_Videos(df)
# result <- correlation_between(df)



result <- channel_Top_10_Liked_Videos(df, "CaseyNeistat")
# result <- channel_Top_Viewed_Video(df, "CaseyNeistat")
# result <- channel_Top_Impression_Video(df, "CaseyNeistat")
print(result)
