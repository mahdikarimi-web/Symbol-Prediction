This notebook provides a simple way to extract Open, High, Low, and Close (OHLC) data for a specified financial symbol using the yfinance library in Google Colab. The script also adjusts datetime values based on the +01:00 timezone and allows for easy downloading of the adjusted data as a CSV file.

Prerequisites:

You need to have the following libraries available in your Google Colab environment:

yfinance
pandas
google.colab

These libraries are usually pre-installed in Google Colab, but you can install any missing packages using the following commands:

    !pip install yfinance pandas

Usage:

    1.Open the Notebook: Create a new notebook in Google Colab.
    2.Copy and Paste the Code: Copy the provided script into a cell in the notebook.
    3.Set Parameters: Define your parameters for data extraction:

    symbol = 'EURUSD=X'  # Replace with your desired financial symbol
    period = '2y'        # Replace with your desired period (e.g., '1y', '2y')
    interval = '1h'      # Use '1d' for daily data or '1h' for hourly data

    4.run the program

Output:

The script will generate a CSV file named esd-[symbol]-[period]-[interval].csv containing the extracted and adjusted OHLC data.
The file will be automatically downloaded to your local machine after execution.

Tips:

In yfinance, valid symbols represent different financial instruments like stocks, currencies, cryptocurrencies, indices, and commodities. Here are examples of valid symbols across categories:

1. Stocks
For individual company stocks, symbols typically match their ticker on exchanges:
Apple: AAPL
Google (Alphabet): GOOG or GOOGL
Tesla: TSLA
Amazon: AMZN
Microsoft: MSFT

2. Currencies
Currency pairs often have the format XXXYYY=X, where XXX is the base currency and YYY is the quote currency:
EUR/USD (Euro to USD): EURUSD=X
GBP/USD (British Pound to USD): GBPUSD=X
USD/JPY (USD to Japanese Yen): JPY=X
USD/CHF (USD to Swiss Franc): CHF=X

3. Cryptocurrencies
Cryptocurrencies are also supported, using similar symbol formatting:
Bitcoin to USD: BTC-USD
Ethereum to USD: ETH-USD
Dogecoin to USD: DOGE-USD

4. Indices
Major stock indices use their specific codes:
S&P 500: ^GSPC
Dow Jones Industrial Average: ^DJI
Nasdaq Composite: ^IXIC
FTSE 100: ^FTSE

5. Commodities
Commodities such as gold or oil:
Gold: GC=F
Crude Oil: CL=F
Silver: SI=F

6. ETFs (Exchange-Traded Funds)
ETFs follow their own tickers:
SPDR S&P 500 ETF Trust: SPY
Invesco QQQ Trust: QQQ

7. Bonds
Government bonds:
US Treasury Bond 10-Year: ^TNX

You can explore more symbols directly on finance.yahoo.com, or through the yfinance search functionality.
