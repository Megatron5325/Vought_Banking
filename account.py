'''
Programmer: Megan Schleicher
Date: 11/20/2023
Revision: 1.0
Description: this class will describe
the methods and attributes of an account
object
'''

class Account:
    """a model of an account"""
    def __init__(self, owner, username, password, account_type):
        self.owner = owner
        self.username = username
        self.password = password
        self.account_type = account_type
