#add import
from question_b import Stock
def stock_purchase_history():
    StockA = Stock("Apple Inc", "AAPL")
    StockB = Stock("Caterpillar","CAT")
    StockC = Stock("Eastman Kodak","EK")
    StockD = Stock("Google","GOOG")
    StockE = Stock("Microsoft","MSFT")
    dictA = {
        StockA.stockSymbol() : StockA.stockName(),
        StockB.stockSymbol() : StockB.stockName(),
        StockC.stockSymbol() : StockC.stockName(),
        StockD.stockSymbol() : StockD.stockName(),
        StockE.stockSymbol() : StockE.stockName()
    }
    print("Stock name Stock symbol")
    for i in dictA:
        print(dictA[i], i)

i=0
while i != 2:
    i = int(input("Stock Purchase Menu\n1-Display stock purchase history\n2-exit\n"))
    if i == 1:
        stock_purchase_history()
        continue