import argparse
import csv
from datetime import datetime, timedelta
import newsapi
from newsapi import NewsApiClient

def get_news_from_newsapi(term):
    news_data = []
    newsapi = NewsApiClient(api_key='4e316ac7e7c94dac84a945ba2c1733f1')
    all_articles = newsapi.get_everything(
        q=term,
        language='en',
    )
    for article in all_articles['articles']:
        timestamp = article['publishedAt']
        title = article['title']
        source = article['source']['name']
        date, time = timestamp.split("T")
        time = time.replace("Z", "")
        news_data.append([term, date, time, source, title])
    return news_data

def save_to_csv(news_data, filename):

    sorted_data = sorted(news_data, key=lambda x: (x[1], x[2]), reverse=True)   
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Topic', 'Date', 'Time', 'Source', 'Title'])
        writer.writerows([row[:5] for row in sorted_data])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch news data based on a specified topic and save to CSV.')
    parser.add_argument('topic', type=str, help='Topic to search for in Google News')
    args = parser.parse_args()

    topic = args.topic
    
    news_data = get_news_from_newsapi(topic)
    
    today = datetime.now().strftime('%Y-%m-%d')
    topic = topic.replace('/', '-')
    filename = f"{topic}_{today}.csv"
    
    save_to_csv(news_data, filename) 
    print(f"Data saved to {filename}.")
