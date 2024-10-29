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
        
        # Calculate the 'pmn' column as the difference between 'nPos' and 'nNeg'
        grouped_df['pmn'] = grouped_df['nPos'] - grouped_df['nNeg']
        
        # Sort by 'Date' to ensure chronological order
        grouped_df = grouped_df.sort_values(by='Date').reset_index(drop=True)
        
        # Initialize the 'action' column with default value 0
        grouped_df['action'] = 0
        
        # Calculate 'action' based on comparison with previous day's 'pmn'
        for i in range(1, len(grouped_df)):
            if grouped_df.loc[i, 'pmn'] > grouped_df.loc[i - 1, 'pmn']:
                grouped_df.loc[i, 'action'] = 1
            elif grouped_df.loc[i, 'pmn'] < grouped_df.loc[i - 1, 'pmn']:
                grouped_df.loc[i, 'action'] = -1
            else:
                grouped_df.loc[i, 'action'] = 0

        # Save the updated DataFrame to a new CSV file
        topic = os.path.splitext(filename)[0]
        output_file_name = f"{topic}_signal.csv"
        output_file_path = os.path.join(output_folder, output_file_name)
        grouped_df.to_csv(output_file_path, index=False)

        print(f"Processed and saved: {output_file_path}")
