'''
Programmer: Megan Schleicher
Date: 11/19/2023
Revision: 1.0
Description: This will be a banking 
interface that will allow a customer to create accounts,
log into old accounts, and withrawel or deposit money
into various accounts.
'''
import getpass
import pickle
import os
import time
from colorama import Fore, Style
from customer import Customer
from bank import Bank

ACCOUNT_TYPE_LIST = ["Soldier Boy Savings", "Crimson Countess Checking",
                     "Stormfront Seniors 401kkk", "Mothers Milk Money Market Fund"]

def exit_program():
    """exits program"""
    exit()

def login():
    """allows user to login and control accounts"""
    print("\nUsername:")
    user_name = input()
    password = getpass.getpass()

    # make list to deliver back to validation method
    creds_list = [user_name, password]
    if check_creds(creds_list) is False:
        print("Login failed, please try again from main menu or create an account")

def create_new_customer():
    """will create new customer object

    Returns:
        Customer: new customer if they don't exist,
        returns none if they do exist trying
        to make another account
    """
    while 1:
        # instansiate Customer class
        customer = Customer()

        # get customer name
        print("\nEnter your full super name. If you enter only first and last," \
            " We'll assume you don't have a middle name.")
        customer.name = get_valid_input("full_name")

        # take name a make sure an existing customer isn't trying to make a new profile
        customer_exists_already = customer_exists(customer.name)
        if customer_exists_already:
            # return None if customer already exists and is trying to make another account
            print("Looks like theres already an account with that name...\n" \
                "Lets try to log you in instead")
            login()
            return None

        # get age
        print("\nHow old are you?\nPlease enter in human years.")
        customer.age = get_valid_input("int")

        # determine if they can pull from their 401k
        if int(customer.age) >= RETIREMENT_WITHDRAWEL_AGE:
            customer.retirment_withdrawel_eligable = True

        # get username
        print("\nEnter a username.\nThe requirements below must be met...\n" \
            f"Length min: {CREDS_MIN}\nLength max: {CREDS_MAX}" \
                "\nNo Spaces")
        customer.username = get_valid_input("username")

        # get password
        print("\nEnter a password.\nThe requirements below must be met...\n" \
            f"Length min: {CREDS_MIN}\nLength max: {CREDS_MAX}" \
                "\nNo spaces")
        customer.password = get_valid_input("password")

        # save account to pickle file
        using_pickle_file("write", customer)

        # let customer know account creation was successful
        Bank.print_and_clear_screen(BANK_BANNER)
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
        Bank.print_and_clear_screen(BANK_BANNER)

        return customer

def mission_statement():
    """prints Vought Banking mission statement"""

    with open(MISSION_STATEMENT_FILE_PATH, "r", encoding="utf8") as f:
        file_contents = f.read()
        Bank.print_and_clear_screen(BANK_BANNER)
        print(Fore.BLUE + file_contents)
        print(Style.RESET_ALL)
        f.close()

# dict for users not logged in
MAIN_MENU_DICT = {
    "Main": go_to_main,
    "Our Mission": mission_statement,
    "Login": login,
    "Exit": exit_program,
    "Create Account": create_new_customer
}

def create_savings():
    """create savings account object"""

def create_checking():
    """create checking account object"""

def create_retirement():
    """create retirement account object"""

def create_mmf():
    """create money market fund account object"""

# dict for creating accounts
ACCOUNT_DICT = {
    "Savings": create_savings,
    "Checking": create_checking,
    "401k": create_retirement,
    "MMF": create_mmf
}

def view_accounts():
    """allows user to view all owned accounts"""

def open_accounts():
    """allows user to open new accounts"""

def delete_account():
    """allows user to delete accounts"""

def withdraw_retirment():
    """allows user to withdraw retirment fund into savings or checking if eligable"""

def logout():
    """takes user back to main page"""

# dict for logged in users
LOGGED_IN_MENU_DICT = {
    "View Accounts": view_accounts,
    "Open New Account": open_accounts,
    "Delete Account": delete_account,
    "Withdraw From Retirment": withdraw_retirment,
    "Logout": logout
}

def check_creds(creds):
    """will take username and password from user and check if user exists"""

    customer = Customer()
    list_of_customers = using_pickle_file("read")

    # check if username and passwrod match any existing customers
    for customer in list_of_customers:
        if customer.username == creds[0]:
            if customer.password == creds[1]:
                return True
        return False

def using_pickle_file(serialization_type = "read", customer = None):
    """deserializes pickle file to get list of customers gor program"""
    #loop through stored objects in pickle file and store in list or read from list
    pickle_command = 'r+b'

    if serialization_type == "write":
        pickle_command = 'w+b'

    with open(PLAYER_FILE_PATH, pickle_command) as file:
        if serialization_type == "read" and os.path.getsize(PLAYER_FILE_PATH) > 0:
            #load existing customer info into list
            list_of_customers = pickle.load(file)
            return list_of_customers

        elif serialization_type == "write":

            # if pickle file has info and you're loading it
            if os.path.getsize(PLAYER_FILE_PATH) > 0:
                # get all existing customers
                list_of_customers = pickle.load(file)
                # append new customer to list
                list_of_customers.append(customer)

            # if pickle file has no info so you're creating new list
            else:
                # no customers exist so creat a list for them
                list_of_customers = []
                # append customer object to list
                list_of_customers.append(customer)

            # store new list in the pickl file
            pickle.dump(list_of_customers, file)
            # close file
            file.close()

            return list_of_customers

def use_logged_in_menu():
    """will bring you back to the logged in menu and wait for user input"""

    # display logged in dict items
    print_logged_in_dict()

    # let user choose option on main menu
    get_valid_input("menu_keys")

def print_logged_in_dict():
    """prints all keys in the logged in dictionary"""

    # user will only reach this point if they logged in successfully
    print("\nLOGIN SUCCESS")
    time.sleep(3)

    # clear screen of main menu
    Bank.print_and_clear_screen(BANK_BANNER)

    print("You can type any menu item\n")
    for key in LOGGED_IN_MENU_DICT:
        print(key)

def main():
    """main entrypoint into program"""
    # instansiate bank
    bank = Bank(MAIN_MENU_DICT, LOGGED_IN_MENU_DICT, BANK_BANNER)
    while 1:
        # clear screen and bring user to main menu
        bank.reset_screen()
        bank.print_main_menu_dict()

        # let user choose option on main menu
        get_valid_input("menu_keys")
        # bring user to logged in menu
        use_logged_in_menu()

if __name__ == "__main__":
    #avoid ctrl C / ctr D error
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        pass
