class Search:

    stocksDict = {}
    with open("Stocks.txt", 'r') as f:
        for line in f:
            line = line.split(", ")
            stocksDict[line[0]] = line[1].replace("\n", "")
    def __init__(self, webPageText):
        self.text = webPageText
        self.matches = []
        self.noDupesMatches = {}
        self.webPageText = []

    def checkBusiness(self, line, index, name, counter):
        name = name.lower()
        if counter != 5: #no company in the stock list has length 5
            if index == 0:  #if we are at the beginning of the line          
            #index == 0 looks useless but for some unkown reason to god himself it skips some businesses.
                #if a business is at the first index of the line list 
                if name in self.stocksDict.values(): 
                   self.matches.append(name)
            #if it's not at the first index of the line list and is a business            
            elif name in self.stocksDict.values(): 
                self.matches.append(name)
            #else it hasn't been found, decrement and add the preceding word to name                                
            else:
                self.checkBusiness(line, index - 1, line[index -1] + " " + name, counter + 1)
        else:
            return None
    def analyze(self):
        for line in self.text:
            line = line.rstrip("\n")
            line = line.split(" ")
            #for each word in the line, starting at EOL
            for x in range(len(line) - 1, -1, -1):
                line[x] = line[x].replace("\'s", "") #parses noun possession 
                self.checkBusiness(line, x, line[x], 0)

        #self.stocksD = self.stocks.split("\n") #put each stock in it's own index

        '''
        This for loop (line 55) removes "businesses" that were added because they equaled a portion 
        of one business in stock.txt
        
        EX: 'industrials' might be a member of matches[] because some company in Stock.txt has 'industrials' in its name 
        but the full company name wasn't in the provided text
        Therefore, only 'industrials' was added because it thinks hey, this is a company. 
        It equals a company name in stocks.txt 
        but in reality, it's only part of a company
        ''' 
        for match in self.matches:
            for stock in self.stocksDict:
                if match == self.stocksDict[stock]:
                    self.noDupesMatches[str(stock)] = str(match)

    
    def returnMatches(self):
        return (self.noDupesMatches)