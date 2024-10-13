import os
import pandas as pd
from pyfin_sentiment.model import SentimentModel

# Initialize pyFin-Sentiment model
model = SentimentModel("small")

# Define paths
merge_data_folder = "./"
sentiment_data_folder = "./"

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
        
        # Calculate sentiment for each title using the SentimentModel
        def process_sentiment(title):
            sentiment_score = model.predict([title])[0]  # Get the sentiment prediction
            # Map sentiment scores to desired values
            if sentiment_score == '2':
                return '0'  # Neutral
            elif sentiment_score == '3':
                return '-1'  # Negative
            return sentiment_score  # Positive ('1')

        # Apply sentiment processing
        df['sentiment'] = df[title_column].apply(process_sentiment)
        
        # Save the modified DataFrame to the "Extract News Sentiment" folder
        output_file = f"{topic}_sentiment.csv"
        output_path = os.path.join(sentiment_data_folder, output_file)
        df.to_csv(output_path, index=False)

        print(f"Processed and saved: {output_file}")
