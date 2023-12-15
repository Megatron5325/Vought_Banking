'''
Programmer: Megan Schleicher
Date: 11/27/2023
Description: This class will be
a menu object
'''

import time
import getpass
from colorama import Fore, Style
from validate import Validate
from customer import Customer
from file_reader import File

class Menu:
    '''model of a menu object'''

    def __init__(self, main_menu_options, logged_in_menu_options, mission_statement_file_path,
                 player_file_path,retirement_withdrawel_age, creds_min, creds_max,
                 loading_character_length, loading_character, loading_character_sleep_timer):

        self.main_menu_options = main_menu_options
        self.logged_in_menu_options = logged_in_menu_options
        self.mission_statement_file_path = mission_statement_file_path
        self.player_file_path = player_file_path
        self.retirement_withdrawel_age = retirement_withdrawel_age
        self.creds_min = creds_min
        self.creds_max = creds_max
        self.loading_character_length = loading_character_length
        self.loading_character = loading_character
        self.loading_character_sleep_timer = loading_character_sleep_timer

    def go_to_main(self):
        '''resets screen and takes user to main menu'''

        print("You can type any menu item\n")
        for item in self.main_menu_options:
            print(item)

    def print_mission_statement(self):
        '''gets mission statement from text file for bank'''
        with open(self.mission_statement_file_path, "r", encoding="utf8") as f:
            file_contents = f.read()
            print(Fore.BLUE + file_contents)
            print(Style.RESET_ALL)
            f.close()

    def login(self):
        '''logs user in with credentials'''

        print("\nUsername:")
        user_name = input()
        password = getpass.getpass()

        # make list to deliver back to validation method
        creds_list = [user_name, password]
        if Validate.check_creds(creds_list, self.player_file_path) is False:
            print("Login failed, please try again from main menu or create an account")

    def exit_program(self):
        '''ends program'''
        exit()

    def create_new_customer(self, bank):
        '''creates new customer with proper credentials'''
        while 1:
            # instansiate Customer class
            customer = Customer()

            # get customer name
            print("\nEnter your full super name. If you enter only first and last," \
                " We'll assume you don't have a middle name.")
            customer.name = Validate.get_valid_input("full_name")

            # take name a make sure an existing customer isn't trying to make a new profile
            customer_exists_already = Validate.customer_exists(customer.name, self.player_file_path)
            if customer_exists_already:
                # return None if customer already exists and is trying to make another account
                print("Looks like theres already an account with that name...\n" \
                    "Lets try to log you in instead")
                return None

            # get age
            print("\nHow old are you?\nPlease enter in human years.")
            customer.age = Validate.get_valid_input("int")

            # determine if they can pull from their 401k
            if int(customer.age) >= self.retirement_withdrawel_age:
                customer.retirment_withdrawel_eligable = True

            # get username
            print("\nEnter a username.\nThe requirements below must be met...\n" \
                f"Length min: {self.creds_min}\nLength max: {self.creds_max}" \
                    "\nNo Spaces")
            customer.username = Validate.get_valid_input("username")

            # get password
            print("\nEnter a password.\nThe requirements below must be met...\n" \
                f"Length min: {self.creds_min}\nLength max: {self.creds_max}" \
                    "\nNo spaces")
            customer.password = Validate.get_valid_input("password")

            # save account to pickle file
            File.using_pickle_file("write", customer, self.player_file_path)

            # let customer know account creation was successful
            bank.print_and_clear_screen(self.main_menu_options)
            print("\nCONGRATULATIONS! You are now one of hundreds of American Sups that\n" \
                "have chosen to support Frederick Vought Foundation by opening an account!\n\n" \
                    "You will be returned to the front page to login now.")

            # simulate loading screen
            i = 1
            while i < self.loading_character_length:
                print(self.loading_character, end='', flush=True)
                time.sleep(self.loading_character_sleep_timer)
                i += 1
            print ("\n")
            bank.print_and_clear_screen(self.main_menu_options)

            return customer

    # def view_accounts():
    #     """allows user to view all owned accounts"""

    # def open_accounts():
    #     """allows user to open new accounts"""

    # def delete_account():
    #     """allows user to delete accounts"""

    # def withdraw_retirment():
    #     """allows user to withdraw retirment fund into savings or checking if eligable"""

    # def logout():
    #     """takes user back to main page"""

    # def create_savings():
    #     """create savings account object"""

    # def create_checking():
    #     """create checking account object"""

    # def create_retirement():
    #     """create retirement account object"""

    # def create_mmf():
    #     """create money market fund account object"""

     # dict for users not logged in
    MAIN_MENU_DICT = {
        "Main": go_to_main,
        "Our Mission": print_mission_statement,
        "Login": login,
        "Exit": exit_program,
        "Create Account": create_new_customer
    }

    # # dict for logged in users
    # LOGGED_IN_MENU_DICT = {
    #     "View Accounts": view_accounts,
    #     "Open New Account": open_accounts,
    #     "Delete Account": delete_account,
    #     "Withdraw From Retirment": withdraw_retirment,
    #     "Logout": logout
    # }

    # # dict for creating accounts
    # ACCOUNT_DICT = {
    #     "Savings": create_savings,
    #     "Checking": create_checking,
    #     "401k": create_retirement,
    #     "MMF": create_mmf
    # }
