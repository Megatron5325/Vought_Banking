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
from bank import Bank

# constants
MENU_OPTIONS_LIST = ["Main", "Our Mission", "Login", "Exit", "Create Account"]
MISSION_STATEMENT_FILE_PATH = 'print_mission_statement.txt'
PLAYER_FILE_PATH = 'pickle_file'
RETIREMENT_WITHDRAWEL_AGE = 67
CREDS_MIN = 6
CREDS_MAX = 10
LOADING_CHARACTER = "*"
LOADING_CHARACTER_LENGTH = 75
LOADING_CHARACTER_SLEEP_TIMER = 0.095

class Menu:
    '''model of a menu object'''

    @staticmethod
    def go_to_main():
        '''resets screen and takes user to main menu'''

        print("You can type any menu item\n")
        for item in MENU_OPTIONS_LIST:
            print(item)

    @staticmethod
    def print_mission_statement():
        '''gets mission statement from text file for bank'''
        with open(MISSION_STATEMENT_FILE_PATH, "r", encoding="utf8") as f:
            file_contents = f.read()
            print(Fore.BLUE + file_contents)
            print(Style.RESET_ALL)
            f.close()

    @staticmethod
    def login():
        '''logs user in with credentials'''

        print("\nUsername:")
        user_name = input()
        password = getpass.getpass()

        # make list to deliver back to validation method
        creds_list = [user_name, password]
        if Validate.check_creds(creds_list, PLAYER_FILE_PATH) is False:
            print("Login failed, please try again from main menu or create an account")

    @staticmethod
    def exit_program():
        '''ends program'''
        exit()

    @staticmethod
    def create_new_customer():
        '''creates new customer with proper credentials'''
        while 1:
            # instansiate Customer class
            customer = Customer()

            # get customer name
            print("\nEnter your full super name. If you enter only first and last," \
                " We'll assume you don't have a middle name.")
            customer.name = Validate.get_valid_input("full_name")

            # take name a make sure an existing customer isn't trying to make a new profile
            customer_exists_already = Validate.customer_exists(customer.name, PLAYER_FILE_PATH)
            if customer_exists_already:
                # return None if customer already exists and is trying to make another account
                print("Looks like theres already an account with that name...\n" \
                    "Lets try to log you in instead")
                return None

            # get age
            print("\nHow old are you?\nPlease enter in human years.")
            customer.age = Validate.get_valid_input("int")

            # determine if they can pull from their 401k
            if int(customer.age) >= RETIREMENT_WITHDRAWEL_AGE:
                customer.retirment_withdrawel_eligable = True

            # get username
            print("\nEnter a username.\nThe requirements below must be met...\n" \
                f"Length min: {CREDS_MIN}\nLength max: {CREDS_MAX}" \
                    "\nNo Spaces")
            customer.username = Validate.get_valid_input("username")

            # get password
            print("\nEnter a password.\nThe requirements below must be met...\n" \
                f"Length min: {CREDS_MIN}\nLength max: {CREDS_MAX}" \
                    "\nNo spaces")
            customer.password = Validate.get_valid_input("password")

            # save account to pickle file
            File.using_pickle_file("write", customer, PLAYER_FILE_PATH)

            # let customer know account creation was successful
            Bank.print_and_clear_screen(MENU_OPTIONS_LIST)
            print("\nCONGRATULATIONS! You are now one of hundreds of American Sups that\n" \
                "have chosen to support Frederick Vought Foundation by opening an account!\n\n" \
                    "You will be returned to the front page to login now.")

            # simulate loading screen
            i = 1
            while i < LOADING_CHARACTER_LENGTH:
                print(LOADING_CHARACTER, end='', flush=True)
                time.sleep(LOADING_CHARACTER_SLEEP_TIMER)
                i += 1
            print ("\n")
            Bank.print_and_clear_screen(MENU_OPTIONS_LIST)

            return customer

    # dict for users not logged in
    MAIN_MENU_DICT = {
        "Main": go_to_main,
        "Our Mission": print_mission_statement,
        "Login": login,
        "Exit": exit_program,
        "Create Account": create_new_customer
    }
