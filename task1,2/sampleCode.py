import pandas as pd
from datetime import datetime, timedelta
"""# Read the CSV file
df = pd.read_csv('final.csv')

# Remove the last 5 columns
df = df.iloc[:, :-5]

# Save the modified DataFrame back to a new CSV file
df.to_csv('main.csv', index=False)
"""
"""
def get_prev_hour(pub_time):
    # Convert the time string to a datetime object
    pub_time_dt = pd.to_datetime(pub_time, format='%H:%M')
    
    # If the minute part is zero, subtract one hour
    if pub_time_dt.minute == 0:
        prev_hour = pub_time_dt - timedelta(hours=1)
    else:
        # Round down to the nearest full hour
        prev_hour = pub_time_dt.replace(minute=0, second=0, microsecond=0)
    
    # Return the formatted time string
    return prev_hour.strftime('%H:%M')

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('main.csv')

# Apply the function to the 'PubTime' column to create a new 'PrevH' column
df['PrevH'] = df['PubTime'].apply(get_prev_hour)

# Save the updated DataFrame back to a CSV file
df.to_csv('main.csv', index=False)

print(df)
"""
"""
df = pd.read_csv('main.csv')

# Combine the 'PubDate' and 'PrevH' columns with a space in between
df['Combined'] = df['PubDate'] + ' ' + df['PrevH']

# Create a new DataFrame with just the combined column
df_combined = df[['Combined']]

# Save the new DataFrame to a new CSV file
df_combined.to_csv('combined.csv', index=False, header=False)

print(df_combined)"""
"""
combined_df = pd.read_csv('combined.csv', header=None, names=['Combined'])
eurusd_df = pd.read_csv('eurusd_data.csv')

# Ensure the Datetime column is a string and take the first 16 characters
eurusd_df['Datetime_trimmed'] = eurusd_df['Datetime'].str[:16]

# Merge the dataframes based on the matching condition
merged_df = pd.merge(combined_df, eurusd_df[['Datetime_trimmed', 'Close']],
                     left_on='Combined', right_on='Datetime_trimmed', how='left')

# Drop the temporary 'Datetime_trimmed' column
merged_df.drop('Datetime_trimmed', axis=1, inplace=True)

# Save the resulting dataframe with the new 'Close' column to a new CSV file
merged_df.to_csv('combined_with_close.csv', index=False)

print(merged_df)"""
'''
# Load the CSV files
main_df = pd.read_csv('main.csv')
combined_with_close_df = pd.read_csv('combined_with_close.csv')

# Get the values from the last column of 'combined_with_close.csv'
# Assuming the last column is 'Close', adjust the name if different
last_col_values = combined_with_close_df.iloc[:, -1]

# Add the values as a new column called 'PrevHIndex' in 'main.csv'
main_df['PrevHIndex'] = last_col_values

# Save the updated DataFrame to 'main.csv'
main_df.to_csv('main2.csv', index=False)

print(main_df)
'''
'''
df = pd.read_csv('main2.csv')

# Combine 'PubDate' and 'PubTime' columns with a space in between
df['Combined'] = df['PubDate'] + ' ' + df['PubTime']

# Create a new DataFrame with just the combined column
df_combined = df[['Combined']]

# Save the new DataFrame to a CSV file
df_combined.to_csv('combined_pubdate_pubtime.csv', index=False, header=False)
'''
'''
combined_df = pd.read_csv('combined_pubdate_pubtime.csv', header=None, names=['Combined'])
eurusd_df = pd.read_csv('eurusd_data.csv')

# Ensure the 'Datetime' column is a string and take the first 16 characters
eurusd_df['Datetime_trimmed'] = eurusd_df['Datetime'].str[:16]

# Merge the two dataframes based on the matching condition
merged_df = pd.merge(combined_df, eurusd_df[['Datetime_trimmed', 'Close']],
                     left_on='Combined', right_on='Datetime_trimmed', how='left')

# Drop the temporary 'Datetime_trimmed' column
merged_df.drop('Datetime_trimmed', axis=1, inplace=True)

# Save the resulting dataframe with the new 'Close' column to a new CSV file
merged_df.to_csv('combined_with_close.csv', index=False)
'''
'''
main2_df = pd.read_csv('main2.csv')
combined_with_close_df = pd.read_csv('combined_with_close.csv')

# Get the values from the last column of 'combined_with_close.csv'
# Assuming the last column is 'Close', adjust the name if it's different
last_col_values = combined_with_close_df.iloc[:, -1]

# Add the values as a new column called 'CurrHIndex' in 'main2.csv'
main2_df['CurrHIndex'] = last_col_values

# Save the updated DataFrame to a new CSV file
main2_df.to_csv('main3.csv', index=False)
'''
'''
def get_next_hour(pub_time):
    # Convert the time string to a datetime object
    pub_time_dt = pd.to_datetime(pub_time, format='%H:%M')
    
    # Round up to the next full hour if not already on the hour
    if pub_time_dt.minute == 0:
        next_hour = pub_time_dt + timedelta(hours=1)
    else:
        next_hour = (pub_time_dt + timedelta(minutes=60 - pub_time_dt.minute)).replace(minute=0, second=0, microsecond=0)
    
    # Return the formatted time string
    return next_hour.strftime('%H:%M')

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('main3.csv')

# Apply the function to the 'PubTime' column to create a new 'NextH' column
df['NextH'] = df['PubTime'].apply(get_next_hour)

# Save the updated DataFrame back to a CSV file
df.to_csv('main4.csv', index=False)
'''
"""
df = pd.read_csv('main4.csv')

# Combine 'PubDate' and 'NextH' columns with a space in between
df['Combined'] = df['PubDate'] + ' ' + df['NextH']

# Create a new DataFrame with just the combined column
df_combined = df[['Combined']]

# Save the new DataFrame to a CSV file
df_combined.to_csv('combined_pubdate_nexth.csv', index=False, header=False)
"""
'''
# Load the CSV files
combined_df = pd.read_csv('combined_pubdate_nexth.csv', header=None, names=['Combined'])
eurusd_df = pd.read_csv('eurusd_data.csv')

# Ensure the 'Datetime' column is a string and take the first 16 characters
eurusd_df['Datetime_trimmed'] = eurusd_df['Datetime'].str[:16]

# Merge the dataframes based on the matching condition
merged_df = pd.merge(combined_df, eurusd_df[['Datetime_trimmed', 'Close']],
                     left_on='Combined', right_on='Datetime_trimmed', how='left')

# Drop the temporary 'Datetime_trimmed' column
merged_df.drop('Datetime_trimmed', axis=1, inplace=True)

# Save the resulting dataframe with the new 'Close' column to a new CSV file
merged_df.to_csv('combined_with_close.csv', index=False)
'''
# Load the CSV files
main4_df = pd.read_csv('main4.csv')
combined_with_close_df = pd.read_csv('combined_with_close.csv')

# Get the values from the last column of 'combined_with_close.csv'
# Assuming the last column is 'Close', adjust the name if it's different
last_col_values = combined_with_close_df.iloc[:, -1]

# Add the values as a new column called 'NextHIndex' in 'main4.csv'
main4_df['NextHIndex'] = last_col_values

# Save the updated DataFrame to a new CSV file
main4_df.to_csv('newfinal.csv', index=False)