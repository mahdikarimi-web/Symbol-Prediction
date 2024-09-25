import yfinance as yf
import pandas as pd
from google.colab import files
import datetime

# Function to extract OHLC data for a given symbol
def extract_symbol_data(symbol, period, interval):
    # Check if the interval is valid
    if interval not in ['1d', '1h']:
        raise ValueError("Invalid interval! Use '1d' for daily or '1h' for hourly.")
    
    # Download the OHLC data
    data = yf.download(tickers=symbol, period=period, interval=interval)
    
    # Prepare the file name
    file_name = f'esd-{symbol.replace("/", "")}-{period}-{interval}.csv'
    
    # Save the data to a CSV file
    data.to_csv(file_name)
    
    return file_name

# Function to adjust datetime values with '+01:00' timezone
def adjust_datetime(file_name):
    # Load the CSV file into a DataFrame
    data = pd.read_csv(file_name)
    
    # Ensure the 'Datetime' column is treated as a datetime object
    data['Datetime'] = pd.to_datetime(data['Datetime'])
    
    # Iterate over the rows and adjust datetime
    for index, row in data.iterrows():
        if row['Datetime'].strftime('%z') == '+0100':  # Check for +01:00 timezone
            # Subtract 1 hour
            adjusted_time = row['Datetime'] - datetime.timedelta(hours=1)
            
            # Update the row's Datetime value
            data.at[index, 'Datetime'] = adjusted_time
    
    # Save the adjusted DataFrame back to a new CSV
    adjusted_file_name = file_name
    data = data.iloc[:, :-1]
    data.to_csv(adjusted_file_name, index=False)
    
    # Download the adjusted CSV
    files.download(adjusted_file_name)

# Main function to extract symbol data and adjust datetime
def main(symbol, period, interval):
    # Step 1: Extract symbol data and save it to a CSV
    file_name = extract_symbol_data(symbol, period, interval)
    
    # Step 2: Adjust datetime values in the CSV if needed
    adjust_datetime(file_name)

# Example usage
symbol = 'EURUSD=X'  # Replace with your desired symbol
period = '2y'        # Replace with your desired period
interval = '1h'      # Use '1d' for daily or '1h' for hourly

main(symbol, period, interval)
