import pandas as pd

# List of file paths for the CSV files
file_paths = [
    "static/datasets/USvideos.csv",
    "static/datasets/RUvideos.csv",
    "static/datasets/CAvideos.csv",
    "static/datasets/DEvideos.csv"
]

# Initialize an empty list to store DataFrames
dataframes = []

# Read and concatenate the CSV files into a single DataFrame
for file_path in file_paths:
    df = pd.read_csv(file_path, encoding='latin1')  # Specify the encoding (e.g., 'latin1')
    dataframes.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

# Print the first 5 rows of the combined DataFrame
print(combined_df.head(5))
