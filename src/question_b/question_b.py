#write functions here, don't add input('') statements here!

class Stock():
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    def stockName(self):
        return self.name
    def stockSymbol(self):
        return self.symbol
    