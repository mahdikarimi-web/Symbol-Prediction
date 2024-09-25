import argparse
import requests
import xml.etree.ElementTree as ET
import csv
from datetime import datetime, timedelta

def get_news_from_rss(term, months_ago=3):
    url = f"https://news.google.com/rss/search?q={term}"
    response = requests.get(url)
    root = ET.fromstring(response.content)
    news_data = []
    cutoff_date = datetime.now() - timedelta(days=months_ago * 30) 
    for item in root.findall('.//item'):
        title = item.find('title').text
        pub_date = item.find('pubDate').text
        source = item.find('source').text if item.find('source') is not None else "No source available"
        pub_date_obj = datetime.strptime(pub_date, '%a, %d %b %Y %H:%M:%S %Z')
        if pub_date_obj >= cutoff_date:
            date = pub_date_obj.strftime('%Y-%m-%d')
            time = pub_date_obj.strftime('%H:%M')
            news_data.append([term, date, time, source, title, pub_date_obj]) 
    return news_data

def save_to_csv(news_data, filename='googlenews.csv', sort_ascending=True):
    news_data.sort(key=lambda x: x[5], reverse=not sort_ascending)  
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Topic', 'Date', 'Time', 'Source', 'Title'])
        writer.writerows([row[:5] for row in news_data])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch news data based on a specified topic and save to CSV.')
    parser.add_argument('topic', type=str, help='Topic to search for in Google News')
    args = parser.parse_args()

    topic = args.topic
    
    news_data = get_news_from_rss(topic)
    
    today = datetime.now().strftime('%Y-%m-%d')
    topic = topic.replace('/', '-')
    filename = f"{topic}_{today}.csv"
    
    save_to_csv(news_data, filename, sort_ascending=False) 
    print(f"Data saved to {filename}.")