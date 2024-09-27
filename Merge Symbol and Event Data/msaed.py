from datetime import timedelta
import pandas as pd

symbolDataFileDaily = 'esd_BTC-USD_2y_1d.csv'
symbolDataFileHourly = 'esd_BTC-USD_2y_1h.csv'
# Read the CSV file
df = pd.read_csv('ecdf.csv')

# Convert 'PubDate' column to datetime format
df['PubDate'] = pd.to_datetime(df['PubDate'])

# Add a new column 'PrevDate' which is one day before 'PubDate'
df['PrevDate'] = df['PubDate'] - pd.DateOffset(days=1)

# Convert 'PrevDate' back to the required format ('YYYY/MM/DD')
df['PrevDate'] = df['PrevDate'].dt.strftime('%Y/%m/%d')

df['NextDate'] = df['PubDate'] + pd.DateOffset(days=1)

# Convert 'NextDate' back to the required format ('YYYY/MM/DD')
df['NextDate'] = df['NextDate'].dt.strftime('%Y/%m/%d')

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


# Apply the function to the 'PubTime' column to create a new 'PrevH' column
df['PrevH'] = df['PubTime'].apply(get_prev_hour)


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

# Apply the function to the 'PubTime' column to create a new 'NextH' column
df['NextH'] = df['PubTime'].apply(get_next_hour)

# Save the updated DataFrame back to a CSV file
df.to_csv('final1.csv', index=False)





df = pd.read_csv(symbolDataFileDaily)

# Remove ' 00:00:00' by converting the first column to just the date string
df[df.columns[0]] = pd.to_datetime(df[df.columns[0]]).dt.strftime('%Y-%m-%d')

# Save the updated DataFrame back to a CSV file
df.to_csv(f'new_{symbolDataFileDaily}', index=False)

print("Time part removed from the first column.")


#===============================================================================
#===============================================================================


final1_df = pd.read_csv('final1.csv')
new_esd_df = pd.read_csv(f'new_{symbolDataFileDaily}')

# Ensure the 'Date' columns are of datetime type for accurate comparison
final1_df['PrevDate'] = pd.to_datetime(final1_df['PrevDate'])
new_esd_df['Date'] = pd.to_datetime(new_esd_df['Date'])

split_parts = symbolDataFileDaily.split('_')
symbol = split_parts[1]

# Iterate through each row in final1_df to find matching dates
for index, row in final1_df.iterrows():
    prev_date = row['PrevDate']
    
    # Check if the date exists in new_esd_df
    if prev_date in new_esd_df['Date'].values:
        # Get the corresponding row from new_esd_df
        matching_row = new_esd_df[new_esd_df['Date'] == prev_date].iloc[0]
        
        # Assign values to the corresponding columns in final1_df
        final1_df.at[index, f'PrevD[{symbol}][O]'] = matching_row['Open']
        final1_df.at[index, f'PrevD[{symbol}][H]'] = matching_row['High']
        final1_df.at[index, f'PrevD[{symbol}][L]'] = matching_row['Low']
        final1_df.at[index, f'PrevD[{symbol}][C]'] = matching_row['Close']


final1_df['NextDate'] = pd.to_datetime(final1_df['NextDate'])
new_esd_df['Date'] = pd.to_datetime(new_esd_df['Date'])

# Iterate through each row in final1_df to find matching dates
for index, row in final1_df.iterrows():
    next_date = row['NextDate']
    
    # Check if the date exists in new_esd_df
    if next_date in new_esd_df['Date'].values:
        # Get the corresponding row from new_esd_df
        matching_row = new_esd_df[new_esd_df['Date'] == next_date].iloc[0]
        
        # Assign values to the corresponding columns in final1_df
        final1_df.at[index, f'NextD[{symbol}][O]'] = matching_row['Open']
        final1_df.at[index, f'NextD[{symbol}][H]'] = matching_row['High']
        final1_df.at[index, f'NextD[{symbol}][L]'] = matching_row['Low']
        final1_df.at[index, f'NextD[{symbol}][C]'] = matching_row['Close']






final1_df['PubDate'] = pd.to_datetime(final1_df['PubDate'])
new_esd_df['Date'] = pd.to_datetime(new_esd_df['Date'])

# Iterate through each row in final1_df to find matching dates
for index, row in final1_df.iterrows():
    pub_date = row['PubDate']
    
    # Check if the date exists in new_esd_df
    if pub_date in new_esd_df['Date'].values:
        # Get the corresponding row from new_esd_df
        matching_row = new_esd_df[new_esd_df['Date'] == pub_date].iloc[0]
        
        # Assign values to the corresponding columns in final1_df
        final1_df.at[index, f'CurrD[{symbol}][O]'] = matching_row['Open']
        final1_df.at[index, f'CurrD[{symbol}][H]'] = matching_row['High']
        final1_df.at[index, f'CurrD[{symbol}][L]'] = matching_row['Low']
        final1_df.at[index, f'CurrD[{symbol}][C]'] = matching_row['Close']

# Save the updated final1_df back to CSV
final1_df.to_csv('final1_updated.csv', index=False) #only with PrevD and NextD and CurrD


#===========================================================================
#===========================================================================


df = pd.read_csv('final1_updated.csv')

# Combine the 'PubDate' and 'PrevH' columns into a new 'combined' column
df['combined'] = df['PubDate'] + ' ' + df['PrevH']

# Create a new DataFrame with just the 'combined' column
df_combined = df[['combined']]

# Save the DataFrame to a new CSV file
df_combined.to_csv('combined.csv', index=False)

print("New CSV file 'combined.csv' created successfully.")




df_combined = pd.read_csv('combined.csv')
df_esd = pd.read_csv('esd_BTC-USD_2y_1h.csv')

# Ensure the DateTime format of the first column in esd_BTC-USD_2y_1h.csv is consistent with 'combined'
df_esd['DateTime'] = df_esd.iloc[:, 0].str[:16]  # First 16 characters

# Create new columns in df_combined for Open, High, Low, Close and initialize with NaN
df_combined['Open'] = None
df_combined['High'] = None
df_combined['Low'] = None
df_combined['Close'] = None

# Loop through the combined DataFrame and check if the 'combined' value matches 'DateTime' in esd file
for i, row in df_combined.iterrows():
    match = df_esd[df_esd['DateTime'] == row['combined']]
    
    if not match.empty:
        # If match is found, extract Open, High, Low, and Close values
        df_combined.at[i, 'Open'] = match['Open'].values[0]
        df_combined.at[i, 'High'] = match['High'].values[0]
        df_combined.at[i, 'Low'] = match['Low'].values[0]
        df_combined.at[i, 'Close'] = match['Close'].values[0]

# Save the updated DataFrame to a new CSV file
df_combined.to_csv('combined_with_esd_data.csv', index=False)

# Load both CSV files into DataFrames
df_final = pd.read_csv('final1_updated.csv')
df_combined_with_esd = pd.read_csv('combined_with_esd_data.csv')
# Add 'Open', 'High', 'Low', and 'Close' columns from 'combined_with_esd_data.csv' to 'final1_updated.csv'
df_final[f'PrevH[{symbol}][O]'] = df_combined_with_esd['Open']
df_final[f'PrevH[{symbol}][H]'] = df_combined_with_esd['High']
df_final[f'PrevH[{symbol}][L]'] = df_combined_with_esd['Low']
df_final[f'PrevH[{symbol}][C]'] = df_combined_with_esd['Close']

# Save the updated DataFrame to a new CSV file
df_final.to_csv('final1_updated_with_PrevH.csv', index=False)