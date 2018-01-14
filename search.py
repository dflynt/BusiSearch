with open("Stocks.txt", 'r') as f, open("example.txt", 'r') as f2:
    stocks = f.read() #load stock list into memory
    def checkBusiness(line, index, name, counter):
        name = name.lower()
        if counter != 5: #no company in the stock list has length 5
            if index == 0:  #if we are at the beginning of the line
                if(stocks.count(name + "\n") == 1): #if a business is at the first index of the line list
                    print(name)
            elif stocks.count(name + "\n") == 1: #if it's not at the first index of the line list and is a business
                print(name)
            else:
                checkBusiness(line, index - 1, line[index -1] + " " + name, counter + 1) #if it hasn't been found, decrement and add the preceding word in the list
        else:
            return None
    for line in f2:
            line = line.split(" ")
            for x in range(len(line) - 1, -1, -1): #for each word in the line, starting at EOL
                line[x] = line[x].replace(".", "").replace(",","").lower() #removes period; takes into account busi names at the ends of sentences
                if(checkBusiness(line, x, line[x], 0) != None): #if it's not a business
                        print(checkBusiness(line, x, line[x], 0))   #print the word
