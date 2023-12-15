'''
Programmer: Megan Schleicher
Date: 11/19/2023
Revision: 1.0
Description: This will be a banking 
interface that will allow a customer to create accounts,
log into old accounts, and withrawel or deposit money
into various accounts.
'''

import pyfiglet
from validate import Validate
from bank import Bank
from menu import Menu

# constants
BANK_BANNER = pyfiglet.figlet_format("Vought Banking")
MISSION_STATEMENT_FILE_PATH = 'print_mission_statement.txt'
PLAYER_FILE_PATH = 'pickle_file'
MIN_NAME_LENGTH = 10
RETIREMENT_WITHDRAWEL_AGE = 67
CREDS_MIN = 6
CREDS_MAX = 10
LOADING_CHARACTER = "*"
LOADING_CHARACTER_LENGTH = 75
LOADING_CHARACTER_SLEEP_TIMER = 0.095
MAIN_MENU_ITEMS = ["Main", "Our Mission", "Login", "Exit", "Create Account"]
LOGGED_MENU_ITEMS = ["View Accounts", "Open New Account", "Delete Account",
                     "Withdraw From Retirement", "Logout"]

def main():
    """main entrypoint into program"""
    # instansiate classes
    menu = Menu(MAIN_MENU_ITEMS, LOGGED_MENU_ITEMS, MISSION_STATEMENT_FILE_PATH, PLAYER_FILE_PATH,
                RETIREMENT_WITHDRAWEL_AGE, CREDS_MIN, CREDS_MAX,
                LOADING_CHARACTER_LENGTH, LOADING_CHARACTER, LOADING_CHARACTER_SLEEP_TIMER)
    bank = Bank(menu, BANK_BANNER)

    while 1:
        # clear screen and bring user to main menu
        bank.reset_screen_print_main_menu()

        # let user choose option on main menu
        Validate.get_valid_input("menu_keys")

        # bring user to logged in menu
        bank.reset_screen_print_logged_menu()

if __name__ == "__main__":
    #avoid ctrl C / ctr D error
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        pass
