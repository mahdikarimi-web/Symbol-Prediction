this program creates a dataset of events using the scraped data that is given to it.
make sure to initialize your csv file address at the top of bed.py in "initial_file" variable.
it will generate the desired dataframe in the current directory as "ecdf.csv"

Output columns:

• PubDate: The date of publishing event

• PubTime: The time of publishing event

• Currency: The currency/country of the event

• Event: The published event

• CurrEvent: The combined value of Currency and Event in the form Currency-Event

• Actual: The actual value of the variable published in the event

• Forecast: The forecasted value of the variable published in the event

• Previous: The Previous value of the variable published in the event
