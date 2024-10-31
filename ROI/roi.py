import sys
import pandas as pd

# Check if enough arguments are provided
if len(sys.argv) != 5:
    print("Usage: python roi.py <esd_BTC-USD-2y_1d.csv> <bitcoin_sentiment_signal.csv> <start-usd-balance> <output.csv>")
    sys.exit(1)

# Read command-line arguments
sdf_file = sys.argv[1]
ssf_file = sys.argv[2]
start_usd_balance = float(sys.argv[3])
output_file = sys.argv[4]

# Load input data
sdf_data = pd.read_csv(sdf_file)
ssf_data = pd.read_csv(ssf_file)

# Initialize the new DataFrame with the required columns
new_df = pd.DataFrame(columns=['Date', 'curr-usd-balance', 'curr-sym-balance', 'next-usd-balance', 'next-sym-balance', 'paction', 'price'])

# Fill the 'Date' column with values from 'Date' column of bitcoin_sentiment_signal.csv
new_df['Date'] = ssf_data['Date']

# Initialize the first row with the starting balance
new_df.loc[0, 'curr-usd-balance'] = start_usd_balance
new_df.loc[0, 'curr-sym-balance'] = 0
new_df.loc[0, 'next-usd-balance'] = start_usd_balance
new_df.loc[0, 'next-sym-balance'] = 0
new_df.loc[0, 'paction'] = float('nan')
new_df.loc[0, 'price'] = float('nan')

# Iterate over each row, starting from the second one
for idx in range(1, len(new_df)):
    # Set current balances based on the previous row's next balances
    new_df.loc[idx, 'curr-usd-balance'] = new_df.loc[idx - 1, 'next-usd-balance']
    new_df.loc[idx, 'curr-sym-balance'] = new_df.loc[idx - 1, 'next-sym-balance']
    
    # Find the action from bitcoin_sentiment_data based on the date of the previous row
    prev_date = new_df.loc[idx - 1, 'Date']
    action_row = ssf_data[ssf_data['Date'] == prev_date]
    if not action_row.empty:
        new_df.loc[idx, 'paction'] = action_row.iloc[0]['action']
    
    # Find the nearest 'close' price from esd_BTC-USD-2y_1d.csv with a date before the current row's date
    curr_date = new_df.loc[idx, 'Date']
    prior_dates = sdf_data[sdf_data['Date'] <= curr_date]
    if not prior_dates.empty:
        new_df.loc[idx, 'price'] = prior_dates.iloc[-1]['Close']  # Ensure column name matches in CSV
    
    # Set next balances based on paction and the trading logic
    paction = new_df.loc[idx, 'paction']
    price = new_df.loc[idx, 'price']
    curr_usd_balance = new_df.loc[idx, 'curr-usd-balance']
    curr_sym_balance = new_df.loc[idx, 'curr-sym-balance']
    
    if pd.notna(paction) and pd.notna(price):
        if paction == 1 and curr_usd_balance > 0:
            new_df.loc[idx, 'next-usd-balance'] = 0
            new_df.loc[idx, 'next-sym-balance'] = curr_usd_balance / price
        elif paction == 1 and curr_usd_balance <= 0:
            new_df.loc[idx, 'next-usd-balance'] = curr_usd_balance
            new_df.loc[idx, 'next-sym-balance'] = curr_sym_balance
        elif paction == -1 and curr_sym_balance > 0:
            new_df.loc[idx, 'next-sym-balance'] = 0
            new_df.loc[idx, 'next-usd-balance'] = curr_sym_balance * price
        elif paction == -1 and curr_sym_balance <= 0:
            new_df.loc[idx, 'next-usd-balance'] = curr_usd_balance
            new_df.loc[idx, 'next-sym-balance'] = curr_sym_balance
        else:
            new_df.loc[idx, 'next-usd-balance'] = curr_usd_balance
            new_df.loc[idx, 'next-sym-balance'] = curr_sym_balance
    else:
        new_df.loc[idx, 'next-usd-balance'] = curr_usd_balance
        new_df.loc[idx, 'next-sym-balance'] = curr_sym_balance

# Save the DataFrame to a CSV file
new_df.to_csv(output_file, index=False)
print(f"Output saved to {output_file}")
