from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import csv
import time

def scroll_down(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Adjust as needed

def click_next_page(driver):
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, '.next')
        next_button.click()
        time.sleep(3)  # Wait for the next page to load
    except:
        return False
    return True

def scrape_google_news(term, months_ago):
    options = Options()
    options.headless = False
    service = Service('C:\\Users\\mahdi\\Desktop\\task3\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)

    url = f"https://news.google.com/search?q={term}&hl=en-US&gl=US&ceid=US%3Aen"
    driver.get(url)

    # Scroll down to load more articles
    for _ in range(20):  # Increased from 5 to 20
        scroll_down(driver)

    # Optional: Paginate through additional pages
    page_count = 0
    max_pages = 5  # Increase this number to scrape more pages
    while click_next_page(driver) and page_count < max_pages:
        for _ in range(10):  # Scroll 10 times on each new page
            scroll_down(driver)
        page_count += 1

    time.sleep(5)  # Adjust as needed

    news_data = []
    cutoff_date = datetime.now() - timedelta(days=months_ago * 30)

    # Find all news results
    results = driver.find_elements(By.CSS_SELECTOR, 'article')

    for result in results:
        try:
            title_element = result.find_element(By.CSS_SELECTOR, '.JtKRv')
            source_element = result.find_element(By.CSS_SELECTOR, '.bInasb')
            time_element = result.find_element(By.CSS_SELECTOR, '.hvbAAd')

            title = title_element.text
            source = source_element.text
            time_str = time_element.get_attribute("datetime")

            pub_date_obj = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%SZ")

            if pub_date_obj >= cutoff_date:
                date = pub_date_obj.strftime('%Y-%m-%d')
                time_val = pub_date_obj.strftime('%H:%M')
                news_data.append([term, date, time_val, source, title, pub_date_obj])
        except Exception as e:
            print(f"Error processing result: {e}")

    driver.quit()
    return news_data

def save_to_csv(news_data, filename='googlenews.csv', sort_ascending=True):
    if not news_data:
        print("No news data to save.")
        return

    news_data.sort(key=lambda x: x[5], reverse=not sort_ascending)
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Search Term', 'Date', 'Time', 'Source', 'Title'])
        writer.writerows([row[:5] for row in news_data])

if __name__ == "__main__":
    search_term = "crude oil inventories"
    months_ago = 24
    news_data = scrape_google_news(search_term, months_ago)
    if news_data:
        save_to_csv(news_data, sort_ascending=False)
        print(f"Data saved to googlenews.csv. Total records: {len(news_data)}")
    else:
        print("No news found.")