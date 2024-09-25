This Python script fetches news data from Google News RSS feed based on a specified topic and saves the data to a CSV file. It allows users to specify a topic as a command-line argument and retrieves news articles related to that topic from the RSS feed.

Usage:

    Run the script with the topic you want to search for in Google News as a command-line argument.
    Example: python news_scraper.py technology

Dependencies:

    The script requires the following Python libraries: argparse, requests, xml.etree.ElementTree, and csv.

Functionality:

    The script fetches news articles from Google News RSS feed for the specified topic.
    It filters the articles based on a specified time frame (default is the last 3 months).
    News data including topic, date, time, source, and title is saved to a CSV file.
    The CSV file is named based on the topic and the current date.

Output:

    The script generates a CSV file containing relevant news data based on the specified topic and saves it in the current directory.

Usage Example:

    python news_scraper.py technology
