#write functions here, don't add input('') statements here!
class Stock():
    def __init__(self, company_name, symbol):
        self.company_name = company_name
        self.symbol = symbol
    def get_company_name(self):
        return self.company_name
    def get_symbol(self):
        return self.symbol