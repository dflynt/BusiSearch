matches = []
noDupesMatches = []
with open("Stocks.txt", 'r') as f, open("example.txt", 'r') as f2:

    stocks = f.read() #load stock list into memory
    def checkBusiness(line, index, name, counter):
        name = name.lower()
        if counter != 5: #no company in the stock list has length 5
            if index == 0:  #if we are at the beginning of the line          
            #index == 0 looks useless but for some reason it skips some businesses.
                #if a business is at the first index of the line list 
                if(stocks.count(name + "\n") == 1): 
                    if(stocks.count(line[index - 1].lower() + " " + name + "\n") == 1):
                        matches.append(line[index - 1].lower() + " " + name)
                    else:
                        matches.append(name)
            #if it's not at the first index of the line list and is a business            
            elif stocks.count(name + "\n") == 1:
                if(stocks.count(line[index - 1].lower() + " " + name + "\n") == 1):
                    matches.append(line[index - 1].lower() + " " + name)
                else:
                    matches.append(name)
            #else it hasn't been found, decrement and add the preceding word to name                                
            else:
                checkBusiness(line, index - 1, line[index -1] + " " + name, counter + 1)
        else:
            return None
    for line in f2:
            line = line.rstrip("\n")
            line = line.split(" ")
            #for each word in the line, starting at EOL
            for x in range(len(line) - 1, -1, -1):
                line[x] = line[x].replace("'s", "") #parses noun possession 
                checkBusiness(line, x, line[x], 0)
    f2.close()
    stocks = stocks.split("\n") #put each stock in it's own index

    '''
    This for loop removes "businesses" that were added because they equaled a portion 
    of one business in stock.txt
    
    EX: 'industrials' is a member of matches[] because some company in Stock.txt has 'industrials' in its name 
    but the full company name wasn't in the provided text
    Therefore, only 'industrials' was added because it thinks hey, this is a company. 
    It equals a company name in stocks.txt 
    but in reality, it's only part of a company
    ''' 
    for match in matches:
        for stock in stocks:
            if match == stock:
                noDupesMatches.append(match)

    #remove duplicates            
    noDupesMatches = set(noDupesMatches)
    '''
    I considered a dictionary to remove duplicates but that would still require checking 
    the entire dictionary to see if the company is in there
    and then check the entire dictionary to get all of the "matches" that 
    are actually in stock.txt and not just like 'industrials' in the example

    I'm using two lists to do this because if I were to do matches.remove(match) 
    it would need n^2 passes worst case 
    to remove all possible duplicates of all possible matches
    to retrieve values: for elem in noDupesMatches
    '''
    print(noDupesMatches)
