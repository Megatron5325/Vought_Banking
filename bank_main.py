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
import getpass
import pickle
import os
from customer import Customer

# constants
BANK_BANNER = pyfiglet.figlet_format("Vought Banking")
MIN_NAME_LENGTH = 2
RETIREMENT_WITHDRAWEL_AGE = 67
PLAYER_FILE_PATH = 'pickle_file'

# dictionary use
def go_to_main():
    """will take customer back to main menu"""

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
    check_creds(creds_list)

# dict for users not logged in
MAIN_MENU_DICT = {
    "Main": go_to_main,
    "Login": login,
    "Exit": exit_program
}

# dict for logged in users
LOGGED_IN_MENU_DICT = {
    "": ""
}

def get_valid_input(validation_type):
    """will continuously prompt user for input
    until input is valid for program

    Args:
        validation_type (datatype): will describe if the
        program needs a string/bool/int/ or a more specific
        type of input

    Return: (dataypes): will return validated user input
    """

    if validation_type == "bool":
        while 1:
            # get user input
            user_input = input()

            # return true if user exists
            if user_input.lower() in ["y", "yes"]:
                return True
            # return false if customer is new
            elif user_input.lower() in ["n", "no"]:
                return False
            else:
                print("...Enter yes or no...")

    if validation_type == "int":
        while 1:
            # get user input
            user_input = input()

            # try to parse
            try:
                int(user_input)
                return user_input

            except ValueError:
                print("Enter a valid number")

    if validation_type == "full_name":
        while 1:
            # get user name
            user_input = input()
            name_list = user_input.split(' ')

            # check to see that they gave you at least a first and last
            if len(name_list) < MIN_NAME_LENGTH:
                print("You must enter a first, last, and middle name if you have one")

            else:
                # modify each part of name
                full_name = ""
                for name in name_list:
                    # lower all parts of name
                    name.lower()
                    # append names to one string and capitalize each one
                    full_name += f"{name.capitalize()} "

                # ensure this is the name they want
                print(f"\nis \"{full_name}\" correct? Type Y/N")

                # validate that their name is correct
                while 1:
                    user_response = input()
                    if user_response.lower() in ["y", "yes"]:
                        return full_name.strip()
                    elif user_response.lower() in ["n", "no"]:
                        break
                    else:
                        print("Enter yes or no...")

            # print statement and continuation for if they want to re-enter their name
            print("Try entering your super human name again.")
            continue

    if validation_type == "username":
        while 1:
            user_input = input()
            if " " in user_input:
                print("Username cannot contain white space")
            else:
                return user_input

    if validation_type == "main_menu_key":
        while 1:
            user_input = input().lower()
            user_input = user_input.capitalize()

            # check to match menu items with user input
            for key, value in MAIN_MENU_DICT.items():
                if user_input == key:
                    value()

            # if what user types doesn't match anything in menu
            print("Type an option on the menu")

def customer_exists(customer_name):
    """determines by name if customer exists already

    Returns:
        bool: true/false depending on if customer exists
    """
    return False

def create_new_customer():
    """will create new customer object

    Returns:
        Customer: new customer if they don't exist,
        returns none if they do exist trying
        to make another account
    """
    # instansiate Customer class
    customer = Customer()

    # get customer name
    print("Enter your full super name. If you enter only first and last," \
          " We'll assume you don't have a middle name.")
    customer.name = get_valid_input("full_name")

    # take name a make sure an existing customer isn't trying to make a new profile
    customer_exists_already = customer_exists(customer.name)
    if customer_exists_already:
        # return None if customer already exists and is trying to make another account
        return None

    # get age
    print("\nHow old are you?\nPlease enter in human years.")
    customer.age = get_valid_input("int")

    # determine if they can pull from their 401k
    if int(customer.age) >= RETIREMENT_WITHDRAWEL_AGE:
        customer.retirment_withdrawel_eligable = True

    return customer

def check_creds(creds):
    """will take username and password from user and check if user exists"""

    customer = Customer()
    #loop through stored objects in pickle file and store in list
    with open(PLAYER_FILE_PATH, 'r+b') as file:
        if os.path.getsize(PLAYER_FILE_PATH) > 0:
            #load existing customer info into list
            list_of_customers = pickle.load(file)

    # check if username and passwrod match any existing customers
    for customer in list_of_customers:
        if customer.username == creds[0]:
            if customer.password == creds[1]:
                return True
        return False


def main():
    """main entrypoint into program"""

    # pyfiglet usage: will dispaly banner for program
    print(BANK_BANNER)
    print("\nWelcome to Vought Banking!")

    # dispaly main menu dict items
    print("You can type any menu item\n")
    for key in MAIN_MENU_DICT:
        print(key)

    # let user choose option on main menu
    get_valid_input("main_menu_key")

    # # determine if customer exists
    # existing_user = get_valid_input("bool")

    # # create new customer or fetch customers existing info
    # if existing_user:   
    #     # let user try to login
    #     login()
    # else:
    #     # create a new customer
    #     print("\nLets get you started")
    #     customer = create_new_customer()

    #     if customer is None:
    #         print("It seems you already have an account and are trying to make a new one.\n" \
    #               "Dont laser your computer...\nLets try logging in first...")

    #         login()

if __name__ == "__main__":
    #avoid ctrl C / ctr D error
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        pass
