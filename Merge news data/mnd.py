import os
import pandas as pd

# Set the directories
source_dir = 'C:\\Users\\mahdi\\Desktop\\works\\extract news data'
target_dir = 'C:\\Users\\mahdi\\Desktop\\works\\Merge news data'

# Ensure the target directory exists
os.makedirs(target_dir, exist_ok=True)

# Function to get the topic from the CSV filename (Assuming topic is part of the filename)
def get_topic(filename):
    # Assuming the topic is part of the filename before any delimiter like underscore (_) or dash (-)
    # Modify this logic if the filename pattern is different
    return filename.split('_')[0]

# Dictionary to hold dataframes for each topic
dataframes_by_topic = {}

# Loop through all CSV files in the source directory
for file in os.listdir(source_dir):
    if file.endswith('.csv'):
        file_path = os.path.join(source_dir, file)
        topic = get_topic(file)  # Extract topic from filename
        
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # If the topic is already in the dictionary, append the new dataframe
        if topic in dataframes_by_topic:
            dataframes_by_topic[topic] = pd.concat([dataframes_by_topic[topic], df], ignore_index=True)
        else:
            dataframes_by_topic[topic] = df

# Merge the dataframes for each topic, remove duplicates, and save the new CSV files
for topic, df in dataframes_by_topic.items():
    df.drop_duplicates(inplace=True)  # Remove duplicate rows
    output_file = os.path.join(target_dir, f'{topic}.csv')  # New merged file
    df.to_csv(output_file, index=False)
    print(f"Merged CSV for topic '{topic}' saved to {output_file}")
