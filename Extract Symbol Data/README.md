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
