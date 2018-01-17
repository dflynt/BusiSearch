from bs4 import BeautifulSoup
from search import Search
import requests
import pprint
text = []
page = requests.get("http://money.cnn.com/2018/01/03/investing/ipo-new-york-wall-street-hong-kong/index.html")
soup = BeautifulSoup(page.content, "html.parser")
for line in soup.find_all("p"):
    text.append(line.get_text())

stock_results = Search(text)
stock_results.analyze()
dict_results = stock_results.returnMatches()
str_Symbols = ""
for k in dict_results.keys():
    str_Symbols = str_Symbols + "," + k

information = requests.get("https://api.iextrading.com/1.0/stock/market/batch?symbols=" + str_Symbols + "&types=quote&filter=symbol,open,close,change,changePercent")
pp = pprint.PrettyPrinter(indent = 4)
pp.pprint(information.json())

