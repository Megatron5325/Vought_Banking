'''
Programmer: Megan Schleicher
Date: 11/20/2023
Revision: 1.0
Description: this class will describe
the methods and attributes of a customer
object
'''

class Customer:
    """a model of a customer"""
    def __init__(self, name = "", age = 0, retirment_withdrawel_eligable = False,
                  list_of_accounts = (), username = "", password = ""):
        self.name = name
        self.age = age
        self.retirment_withdrawel_eligable = retirment_withdrawel_eligable
        self.list_of_accounts = list_of_accounts
        self.username = username
        self.password = password
