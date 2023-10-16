# # Replace 'train.csv' with the actual path to your CSV file
# # csv_file_path <- 'train.csv'

# csv_file_path <- 'static/datasets/USvideos.csv'


# # Load the CSV file into a data frame
# df <- read.csv(csv_file_path)

# # Now you can work with the data frame 'df'
# head(df)  # Display the first few rows of the data frame
    

# Replace 'your_file.csv' with the actual path to your CSV file
csv_file_path <- 'static/datasets/USvideos.csv'

# Load the CSV file into a data frame
df <- read.csv(csv_file_path, encoding = 'latin1')

# Print the first few rows of the data frame to verify its contents
head(df)

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

# Example usage of the functions
result <- top_5_categories(df)
print(result)
