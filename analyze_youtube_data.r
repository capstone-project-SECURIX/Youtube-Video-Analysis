# Load the required library
# library(data.table)

# Read the CSV file into a data frame
# df <- fread("static/datasets/USvideos.csv")

# Replace 'train.csv' with the actual path to your CSV file
csv_file_path <- 'static/datasets/USvideos.csv'
# csv_file_path <- 'static/datasets/RUvideos.csv'
# csv_file_path <- 'static/datasets/CAvideos.csv'
# csv_file_path <- 'static/datasets/DEvideos.csv

# Load the CSV file into a data frame
df <- read.csv(csv_file_path,  encoding='latin1')

# head(df)

print("R file printing : file ------ ")
print(csv_file_path)


# Define a category mapping
category_mapping <- list(
  "1" = "Film & Animation",
  "2" = "Autos & Vehicles",
  "10" = "Music",
  "15" = "Pets & Animals",
  "17" = "Sports",
  "18" = "Short Movies",
  "19" = "Travel & Events",
  "20" = "Gaming",
  "21" = "Videoblogging",
  "22" = "People & Blogs",
  "23" = "Comedy",
  "24" = "Entertainment",
  "25" = "News & Politics",
  "26" = "Howto & Style",
  "27" = "Education",
  "28" = "Science & Technology",
  "29" = "Nonprofits & Activism",
  "30" = "Movies",
  "31" = "Anime/Animation",
  "32" = "Action/Adventure",
  "33" = "Classics",
  "34" = "Comedy",
  "35" = "Documentary",
  "36" = "Drama",
  "37" = "Family",
  "38" = "Foreign",
  "39" = "Horror",
  "40" = "Sci-Fi/Fantasy",
  "41" = "Thriller",
  "42" = "Shorts",
  "43" = "Shows",
  "44" = "Trailers"
)

# Function to get the top 5 categories with the most videos
top_5_categories <- function(df) {
  # Get the top 5 categories and their counts
  top_categories <- as.data.frame(table(df$category_id))

#   topcatvar <- function(cat_id) category_mapping[as.character(cat_id)]
  # Map category IDs to names
  top_categories$category_id <- sapply(top_categories$category_id, function(cat_id) category_mapping[as.character(cat_id)])

  # Rename columns
  colnames(top_categories) <- c("Category", "Count")
  # Convert to a list
  jsondata <- as.list(top_categories)
  return(jsondata)
}

# Function to get the top 10 videos with the most likes
top_10_liked_videos <- function(df) {
  top_rated_videos <- df[order(-df$likes), ][1:10, ]
  # Extract relevant columns
  top_rated_videos <- top_rated_videos[, c("title", "likes")]
  # Convert to a list
  jsondata <- as.list(top_rated_videos)
  return(jsondata)
}

# Function to get the top 10 videos with the most views
top_10_most_viewed_videos <- function(df) {
  top_viewed_videos <- df[order(-df$views), ][1:10, ]
  # Extract relevant columns
  top_viewed_videos <- top_viewed_videos[, c("title", "views")]
  # Convert to a list
  jsondata <- as.list(top_viewed_videos)
  return(jsondata)
}

# Function to calculate the correlation
# between views, likes, dislikes, and comments

correlation_between <- function(df) {
  correlation_datavar <- c("views", "likes", "dislikes", "comment_count")
  correlation_matrix <- cor(df[, correlation_datavar])
  # Convert to a data frame
  correlation_data <- as.data.frame(correlation_matrix)
  return(correlation_data)
}

  # Example usage of the functions
result <- top_5_categories(df)
# result <- top_10_liked_videos(df)
# result <- top_10_most_viewed_videos(df)
# result <- correlation_between(df)

result <- top_5_categories(df)
print(result)