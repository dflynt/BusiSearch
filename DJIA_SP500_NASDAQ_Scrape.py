import requests, bs4, csv
stocks = []

'''
The data for both the S&P500 and the Dow Jones Industrial Average is
gathered from their respective wikipedia pages and then added to the above
stocks list.
'''
djiaStock = requests.get("https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average")
djiaStock.raise_for_status()
djiaStockSoup = bs4.BeautifulSoup(djiaStock.text, "html.parser")
tableElem = djiaStockSoup.find_all('table', class_="wikitable sortable" )[0]

for row in tableElem.findAll('tr')[1:]:
    company = ""
    for data in row.findAll('td'): 
        company = company + "," + data.text
    company = company.split(",")
    stocks.append(company[1])

sp500Stock = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
sp500Stock.raise_for_status()
sp500StockSoup = bs4.BeautifulSoup(sp500Stock.text, "html.parser")
tableElem = sp500StockSoup.find_all('table', class_="wikitable sortable" )[0]

for row in tableElem.findAll('tr')[1:]:
    company = ""
    for data in row.findAll('td'): 
        company = company + "," + data.text
    company = company.split(",")
    stocks.append(company[2])

#NASDAQ data is retrieved from a CSV file
with open("../companylist.csv", 'r') as csvfile:
    stockReader = csv.reader(csvfile)
    for row in stockReader:
        stocks.append(row[1])
csvfile.close()

#Removes duplicates and sorts the final result. I could have ran through the list and put unique values
#in a map but programmers are lazy.
stocks = set(stocks)
stocks = list(stocks)
stocks.sort()

with open('Stocks.txt', 'w') as f:
    for x in stocks:
        f.write(x + "\n")
f.close()