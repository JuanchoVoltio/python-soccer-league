class BankProduct:
    def __init__(self, number, name):
        self.name = name
        self.number = number

    def getTransactionLog(self):
        print('Mustra ultimas 5 transacciones')

#==============================================
class CreditCard(BankProduct):
    def __init__(self, number, name, default_split, expiration_date):
        #BankProduct.__init__(self, number, name)#CONSTRUCTOR DEL PADRE
        super().__init__(number,name)
        self.default_split = default_split
        self.expiration_date = expiration_date

    def getTransactionLog(self):
        print('Mustra ultimos 5 transacciones y el numero de cuotas')

#===============================================
class SavingAccount(BankProduct):
    pass
#===============================================

class Portfolio:
    def __init__(self, products):
        self.products = products

    def showProducts(self):
        for current_product in self.products:
            print(type(current_product))


#===================================================

my_product = CreditCard(123456, "Daniel ", 6, "12-2021")      
print(my_product.getTransactionLog()) 


my_other_product = SavingAccount("323", "Cuenta de ahorros")
products = (my_product, my_other_product)
Portfolio(products).showProducts()

