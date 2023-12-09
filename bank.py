'''
Programmer: Megan Schleicher
Date: 11/20/2023
Revision: 1.0
Description: this class will describe
the methods and attributes of a bank
object
'''

import os
import pyfiglet
from colorama import Fore, Style
from customer import Customer

BANK_BANNER = pyfiglet.figlet_format("Vought Banking")

class Bank:
    """a model of a bank"""

    def __init__(self, main_menu_dict, logged_in_dict, company_banner):
        self.main_menu_dict = main_menu_dict
        self.logged_in_dict = logged_in_dict
        self.company_banner = company_banner

    @staticmethod
    def print_and_clear_screen(menu_options):
        """prints pyfiglet banner"""

        # pyfiglet usage: will display banner for program
        os.system("clear")
        print(Fore.BLUE + BANK_BANNER)
        print(Style.RESET_ALL)

        print("You can type any menu item\n")
        for item in menu_options:
            print(item)
