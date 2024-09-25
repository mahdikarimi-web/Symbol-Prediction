This project processes CSV files containing news articles to calculate sentiment scores for each article's title using the VADER sentiment analysis tool. The output is saved as new CSV files with the calculated sentiment scores.

Prerequisites:

Python 3.x

Pandas library

VADER Sentiment library

You can install the required libraries using pip:

    pip install pandas vaderSentiment

Usage"

1. Prepare your data: Place your CSV files containing news articles in the Merge news data folder. Ensure that the last column of each CSV file contains the article titles.

2. Run the script: Execute the script to process the CSV files and generate sentiment scores:

        python ens.py

3. Output: The processed CSV files with sentiment scores will be saved in the Extract News Sentiment folder. Each output file will be named as topic-sentiment.csv, where topic is derived from the input filename.
