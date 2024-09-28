import os
import pandas as pd

# Define the directories
input_folder = '../Extract News Sentiment'  # Folder containing the input CSV files
output_folder = '../Build sentiment signal'  # Folder to save the output CSV files

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop through all CSV files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        # Construct full file path
        input_file_path = os.path.join(input_folder, filename)
        
        # Load the CSV file
        df = pd.read_csv(input_file_path)
        
        # Group by 'Topic' and 'Date' and calculate the required fields
        grouped_df = df.groupby(['Topic', 'Date']).agg(
            nNews=('sentiment', 'size'),
            nPos=('sentiment', lambda x: (x > 0).sum()),
            nNeg=('sentiment', lambda x: (x < 0).sum()),
            meansen=('sentiment', 'mean')
        ).reset_index()
        
        topic = os.path.splitext(filename)[0]
        
        output_file_name = f"{topic}_signal.csv"
        output_file_path = os.path.join(output_folder, output_file_name)
        grouped_df.to_csv(output_file_path, index=False)

        print(f"Processed and saved: {output_file_path}")
