import requests, bs4

djiaStock = requests.get("https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average")
djiaStock.raise_for_status()
djiaStockSoup = bs4.BeautifulSoup(djiaStock.text, "html.parser")
tableElem = djiaStockSoup.find_all('table', class_="wikitable sortable" )[0]
stocks = []

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

stocks.sort()

with open('Stocks.txt', 'w') as f:
    for x in stocks:
        f.write(x + "\n")
f.close()