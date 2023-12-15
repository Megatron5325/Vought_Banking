'''
Programmer: Megan Schleicher
Date: 11/20/2023
Revision: 1.0
Description: this class will describe
the methods and attributes of a bank
object
'''

import os
import time
from colorama import Fore, Style

class Bank:
    """a model of a bank"""

    def __init__(self, menu, company_banner):
        self.menu = menu
        self.company_banner = company_banner

    def reset_screen_print_main_menu(self):
        """prints pyfiglet banner"""

        # pyfiglet usage: will display banner for program
        os.system("clear")
        print(Fore.BLUE + self.company_banner)
        print(Style.RESET_ALL)

        print("You can type any menu item\n")
        for item in self.menu.main_menu_options:
            print(item)

    def reset_screen_print_logged_menu(self):
        """prints all keys in the logged in dictionary"""

        # user will only reach this point if they logged in successfully
        print("\nLOGIN SUCCESS")
        time.sleep(3)

        # clear screen of main menu
        # pyfiglet usage: will display banner for program
        os.system("clear")
        print(Fore.BLUE + self.company_banner)
        print(Style.RESET_ALL)

        print("You can type any menu item\n")
        for item in self.menu.main_menu_options:
            print(item)
