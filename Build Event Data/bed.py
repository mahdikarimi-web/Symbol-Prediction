import csv
import os
import time
initial_file = "ec.csv"


import pandas as pd
def detect_double_quotes_in_csv(file_path, output_path):
    with open(file_path, mode='r', encoding='latin-1') as file, open(output_path, mode='w', encoding='utf-8') as output_file:
        str_line = ""
        for line in file:
            if '"' in line:
                str_line = line[:-8]
                continue
            output_file.write(str_line + line)

def remove_invalid_characters(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8', newline='') as infile, \
         open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            # Remove occurrences of '��' from each cell in the row
            cleaned_row = [cell.replace('��', '') for cell in row]
            writer.writerow(cleaned_row)
detect_double_quotes_in_csv(initial_file, 'output_file.csv')


input_csv = 'output_file.csv'
output_csv = 'final.csv'
remove_invalid_characters(input_csv, output_csv)





input_file = 'final.csv'
output_file = 'final2.csv'
with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write the header if present
    header = next(reader)
    writer.writerow(header)

    # Iterate through rows and skip rows where the 4th column contains 'Holiday'
    for row in reader:
        if row[3] != 'Holiday':  # 4th column is index 3
            writer.writerow(row)
def remove_empty_last_column(input_file, output_file):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if row[-1] == "":
                row = row[:-1]  # Remove the last column if it is empty
            writer.writerow(row)
input_file = 'final2.csv'
output_file = 'final3.csv'
remove_empty_last_column(input_file, output_file)
with open(output_file, 'r+') as file:
    lines = file.readlines()
    file.seek(0)
    for line in lines:
        if line.endswith(',\n'):
            file.write(line[:-2] + '\n')
        else:
            file.write(line)
    file.truncate()

input_file = 'final3.csv'
output_file = 'final4.csv'
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        del row[3]  # Remove the 4th column (Python uses 0-based indexing)
        writer.writerow(row)

def remove_special_spaces_from_third_column(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            if len(row) >= 3:
                # Replace non-breaking spaces and regular spaces
                row[2] = row[2].replace('\xa0', '').replace('  ', '').strip()  
            writer.writerow(row)

input_file = 'final4.csv'
output_file = 'final5.csv'

remove_special_spaces_from_third_column(input_file, output_file)

def clean_third_column(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if len(row) >= 3:
                # Replace 'ï¿½ï¿½' with an empty string in the third column
                row[2] = row[2].replace('ï¿½ï¿½', '')
                row[3] = row[3].replace('ï¿½ï¿½', '')
            writer.writerow(row)

# File paths
input_csv = 'final5.csv'   # Input CSV file path
output_csv = 'final6.csv' # Output CSV file path

# Call the function to clean the CSV file
clean_third_column(input_csv, output_csv)

def convert_value(value):
    try:
        if 'K' in value:
            # Handle 'k' for thousands, rounding to 2 decimal places
            return round(float(value.replace('K', '')) * 1000, 2)
        elif 'M' in value:
            # Handle 'M' for millions, rounding to 2 decimal places
            return round(float(value.replace('M', '')) * 1000000, 2)
        elif '%' in value:
            # Handle '%' by converting percentage to a decimal and rounding to 3 decimal places
            return round(float(value.replace('%', '')) / 100, 3)
        else:
            # Return the original value if no conversion is needed
            return value
    except ValueError:
        # Handle any conversion errors
        return value

# Function to process the last three columns
def modify_last_three_columns(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if len(row) >= 3:
                # Modify the last three columns (i.e., row[-3], row[-2], row[-1])
                row[-3] = convert_value(row[-3])
                row[-2] = convert_value(row[-2])
                row[-1] = convert_value(row[-1])
            writer.writerow(row)

# File paths
input_csv = 'final6.csv'   # Input CSV file path
output_csv = 'final7.csv' # Output CSV file path

# Call the function to modify the CSV file
modify_last_three_columns(input_csv, output_csv)

months = ['(Jan)', '(Jul)', '(Feb)', '(Aug)', '(Mar)', '(Sep)', 
          '(Apr)', '(Oct)', '(May)', '(Nov)', '(Jun)', '(Dec)']
lims = ['(Q1)','(Q2)','(Q3)','(Q4)']
# Function to clean the fourth column
def clean_fourth_column(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if len(row) >= 4:
                # Remove the month strings from the fourth column
                for month in months:
                    row[3] = row[3].replace(month, '')
                for lim in lims:
                    row[3] = row[3].replace(lim,'')
            writer.writerow(row)

# File paths
input_csv = 'final7.csv'   # Input CSV file path
output_csv = 'final8.csv' # Output CSV file path

# Call the function to clean the CSV file
clean_fourth_column(input_csv, output_csv)
# Specify the column headers to be added
new_columns = ['PubDate', 'PubTime', 'Currency', 'Event', 'Actual', 'Forecast', 'Previous']

# Input and output file paths
input_file = 'final8.csv'
output_file = 'final9.csv'

# Read the content of the input CSV file
with open(input_file, 'r', newline='') as infile:
    reader = csv.reader(infile)
    rows = list(reader)

# Add the new column headers to the first row
rows.insert(0, new_columns)

# Write the modified content to a new CSV file
with open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(rows)
    
# Load the CSV file
df = pd.read_csv('final9.csv')

# Combine Currency and Event columns into a new column CurrEvent
df['CurrEvent'] = df['Currency'] + '-' + df['Event']

# Save the updated DataFrame back to a new CSV file
df.to_csv('final10.csv', index=False)


# Load your CSV file
df = pd.read_csv('final10.csv')

# Convert the first column to datetime format and then to 'YYYY/MM/DD' format
df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0], format='%A, %B %d, %Y').dt.strftime('%Y/%m/%d')

# Save the updated dataframe back to CSV
df.to_csv('ecdf.csv', index=False)

folder_path = os.getcwd()

# List all files in the current folder
for file_name in os.listdir(folder_path):
    # Check if the file is a CSV file and not 'ec.csv' or 'ecdf.csv'
    if file_name.endswith('.csv') and file_name not in ['ec.csv', 'ecdf.csv']:
        # Construct the full file path
        file_path = os.path.join(folder_path, file_name)
        # Remove the file
        os.remove(file_path)
    