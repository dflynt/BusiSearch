import csv
stocks = []
items_to_remove = ["corporation", "company", "inc", "inc.", "corp.", "corp,", "Co.", "co.", "Co", "co",
                    ".com", ".net", "capital", "financial", "ltd", "Ltd", "ltd.", "Ltd.", "lp", "(the)", "the", "limited", "partnership"]
def checkRow(row):
        name = row[1].lower()
        name = name.split(" ")
        company = [n for n in name if n not in items_to_remove]
        company = " ".join(company)
        stocks.append(company.replace(",","").replace(".","").replace("com", "").replace(".net", ""))
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

stocks = set(stocks)
stocks = list(stocks)
stocks.sort()
print(len(stocks))
with open("Stocks.txt", 'w') as f:
    for x in stocks:
        f.write(x + "\n")
f.close()