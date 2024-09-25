import os
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Define paths
merge_data_folder = "C:\\Users\\mahdi\\Desktop\\works\\Merge news data"
sentiment_data_folder = "C:\\Users\\mahdi\\Desktop\\works\\Extract News Sentiment"

# Create the sentiment data folder if it doesn't exist
if not os.path.exists(sentiment_data_folder):
    os.makedirs(sentiment_data_folder)

# Iterate through each CSV file in the "Merge news data" folder
for filename in os.listdir(merge_data_folder):
    if filename.endswith(".csv"):
        # Determine the topic from the filename
        topic = os.path.splitext(filename)[0]
        
        # Load the CSV file
        file_path = os.path.join(merge_data_folder, filename)
        df = pd.read_csv(file_path)

        # Assume the last column is the title
        title_column = df.columns[-1]
        
        # Calculate sentiment for each title
        df['sentiment'] = df[title_column].apply(lambda title: analyzer.polarity_scores(title)['compound'])
        
        # Save the modified DataFrame to the "Extract News Sentiment" folder
        output_file = f"{topic}_sentiment.csv"
        output_path = os.path.join(sentiment_data_folder, output_file)
        df.to_csv(output_path, index=False)

        print(f"Processed and saved: {output_file}")
