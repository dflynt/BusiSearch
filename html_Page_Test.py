from bs4 import BeautifulSoup
from search import Search
import requests
text = []
page = requests.get("http://money.cnn.com/2018/01/03/investing/ipo-new-york-wall-street-hong-kong/index.html")
soup = BeautifulSoup(page.content, "html.parser")
for line in soup.find_all("p"):
    text.append(line.get_text())

stock_results = Search(text)
stock_results.analyze()
print(stock_results.returnMatches())
