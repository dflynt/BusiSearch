import csv
stocks = {}
items_to_remove = ["corporation", "company", "company,", "inc", "inc.", "inc.,", 
                    "corp", "co", "&", "(", " & co", "and co.", "& co.",
                    ".com", ".net", "capital", "financial", "ltd", "lp", "llc", "(the)", "the", "limited",
                    "partnership", "incorporated","companies", "incorporated", "solutions", "technology", "technologies",
                    "fund", "trust", "plc", ]
def checkRow(row):
    symbol = row[0]
    name = row[1].lower()
    name = name.replace("\n", "").replace(",","").replace(".com","").replace(".net", "").replace(".", "")
    name = name.split(" ")
    company = [n for n in name if n.lower() not in items_to_remove]
    company = " ".join(company)
    stocks[symbol.rsplit(" ")] = company #inc isn't removed above for unknown reason
with open("companylist.csv", 'r') as csvfile:
    stockReader = csv.reader(csvfile)
    for row in stockReader:
        checkRow(row)
csvfile.close()

with open("companylist (1).csv", 'r') as csvfile2:
    stockReader = csv.reader(csvfile2)
    for row in stockReader:
        checkRow(row)
csvfile2.close()

with open("companylist (2).csv", 'r') as csvfile3:
    stockReader = csv.reader(csvfile3)
    for row in stockReader:
        checkRow(row)       
csvfile3.close()

with open("Stocks.txt", 'w') as f:
    for x in stocks:
        f.write(x + ", " + stocks[x] + "\n")
f.close()