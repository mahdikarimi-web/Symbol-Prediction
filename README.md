Here is a series of tasks for experimental prediction of symbols used in trading.

1. Folder name: Extract Symbol Data
   Program esd.py extracts a symbol OHLC data. It needs the following two parameters:
   • Symbol: Name of symbol to extract such as: EUR/USD, BitCoin
   
   • Period: Frequency of extraction such as: d(daily), h(Hourly)
   
   • Duration: Number of days of extraction such as: 730d
   
   The output file name is: esd-[symbol]-[period]-[duration].csv
   
   Output columns:
   • Datetime: Date and time of symbol price
   
   • Open: The Openning price of symbol
   
   • High: The Highest price in the period
   
   • Low: The lowest price in the period
   
   • Close: The closing price in the period
   
   • AdjClose: The adjusted price in the period

3. Folder name: Build Event Data
   Program bed.py creates a dataset of events using the scraped data from address: https://www.investing.com/economic-calendar/
   The scraped data should be given in the csv format with the file name: ec.csv with the time zone UTC+0
   The output is sored in ecdf.csv
   Output columns:
   • PubDate: The date of publishing event
   
   • PubTime: The time of publishing event
   
   • Currency: The currency/country of the event
   
   • Event: The published event
   
   • CurrEvent: The combined value of Currency and Event in the form Currency-Event
   
   • Actual: The actual value of the variable published in the event
   
   • Forecast: The forecasted value of the variable published in the event
   
   • Previous: The Previous value of the variable published in the event
   

5. Folder name: Merge Symbol and Event Data
   Program msaed.py merges symbol and event data to create an integrated data set.
   All the csv files in [Extract Symbol Data] folder are merged with the ecdf.csv in folder [Build Event Data] to create ecsymdf.csv
   New output columns added to ecdf.csv are:
   
   • PrevDate: The Date before publishing event
   
   • NextDate: The Date after publishing event
   
   • PrevH: The hour before publishing event (If it has dime will use floor)
   
   • NextH: The hour after publishing event (if it has dime will use celling)
   

• PrevD[-Symbol][-O|H|L|C]: The value of symbol at PrevDate for O or H or L or C

• NextD[-Symbol][-O|H|L|C]: The value of symbol at NextDate for O or H or L or C

• CurrD[-Symbol][-O|H|L|C]: The value of symbol at PubDate for O or H or L or C


• PrevH[-Symbol][-O|H|L|C]: The value of symbol at PrevH for O or H or L or C

• NextH[-Symbol][-O|H|L|C]: The value of symbol at NextH for O or H or L or C

• CurrH[-Symbol][-O|H|L|C]: The value of symbol at PubTime for O or H or L or C

4. Folder name: Extract news data
   Program end.py extract news titles for a specific topic from news sites.
   
   The input parameters are:
   
   • Topic: the terms used to search for news titles
   
   The output is a csv file with the name: [topic]-[date].csv
   
   The columns of output file are:
   
   • Topic: the topic used for search
   
   • Date: the date of publishing news
   
   • Time: the time of publishing news
   
   • Source: the publishing source
   
   • Title: the Title of the news

6. Folder name: Merge news data
   Program mnd.py merges all news data existing in folder [Extract news data] to separate files.
   
   The output is one or more csv file with the name: [topic].csv
   
   All the existing csv files about specific topic are merged into one csv file and duplicates are dropped.

8. Folder name: Extract News Sentiment
   Program ens.py extract sentiment for each news files gathered in folder [Merge news data]. It uses VADER sentiment analyzer.
   
   Output file name: [topic]-sentiment.csv
   
   Output file columns added:
   
   • Sentiment: Sentiment of the title which is a number between -1 and +1

10. Folder name: Build sentiment signal
   Program bss.py builds a daily signal of sentiment data for a specific topic.

   All the sentiment files in folder [Extract News Sentiment] are processed.
   
   Output file name: [topic]-sentiment-signal.csv
   
   Output file columns:
   
   • Topic
   
   • Date
   
   • nNews: number of news published at specific date
   
   • nPos: Number of positive sentiments
   
   • nNeg: Number of negative sentiments
   
   • meansen: Mean of sentiment
