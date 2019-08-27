# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:18:53 2017

@author: vsankar.la
"""

class CreditCard:
    """ A consumer credit card"""
    
    def __init__(self,customer,bank,account,limit):
        """Create a new credit card object"""
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit =   limit
        self._balance = 0
        
    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank    
    
    def get_account(self):
        return self._account
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance+=price
            return True
    
    def makePayment(self,amount):
        self._balance-=amount


if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('Vishnu','BOA','5391 0375 9387 5309',4000))
    wallet.append(CreditCard('Meera','Chase','5391 0375 9387 1234',3000))
    wallet.append(CreditCard('Nandhu','CreditOne','2222 0375 9387 0000',2000))
    wallet.append(CreditCard('Maalu','FirstTech','4440 0375 9387 2341',1000))
    
    
    for val in range(20,41):
        for i in (range(len(wallet))):
            wallet[i].charge(val*(i+1))
            
    
    for i in (range(len(wallet))):
        print()
        
            
