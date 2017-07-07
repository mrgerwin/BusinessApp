from decimal import *

TWOPLACES = Decimal(10)**-2


class Customer:
    def __init__(self, idNum, fnam, lnam, balance):
        self.idNum = idNum
        self.fnam = fnam
        self.lnam = lnam
        self.balance = Decimal(balance).quantize(TWOPLACES)

    def __str__(self):
        return "#" + str(self.idNum)+ " " + self.fnam+ " " + self.lnam+ " with $" +str(self.balance)

    def setBalance(self, amount):
        if type(amount) is float:
            self.balance = Decimal(amount).quantize(TWOPLACES)

    def setId(self, num):
        if type(num) is int:
            self.idNum = num

    def getId(self):
        return self.idNum

    def getBalance(self):
        return self.balance



    
