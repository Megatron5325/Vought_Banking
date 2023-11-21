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
import keyboard
import pyfiglet
from customer import Customer

# constants
BANK_BANNER = pyfiglet.figlet_format("Vought Banking")
MIN_NAME_LENGTH = 2
RETIREMENT_WITHDRAWEL_AGE = 67
PLAYER_FILE_PATH = 'pickle_file'
ACCOUNT_TYPE_LIST = ["Soldier Boy Savings", "Crimson Countess Checking", "Stormfront Seniors 401k",
                      "Mothers Milk Money Market Fund"]
CREDS_MIN = 6
CREDS_MAX = 10

# dictionary uses
def go_to_main():
    """will take customer back to main menu"""
    print_main_menu_dict()

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
    print("\nCongratulations! You are now one of hundreds of American Sups that\n" \
          "have chosen to support Frederick Vought Foundation by opening an account!\n\n" \
            "You will be returned to the front page to login now.")

    return customer

# dict for users not logged in
MAIN_MENU_DICT = {
    "Main": go_to_main,
    "Login": login,
    "Exit": exit_program,
    "Create Account": create_new_customer
}

def create_savings():
    """create savings account object"""
    pass

def create_checking():
    """create checking account object"""
    pass

def create_retirement():
    """create retirement account object"""
    pass

def create_mmf():
    """create money market fund account object"""
    pass

# dict for creating accounts
ACCOUNT_DICT = {
    "Savings": create_savings,
    "Checking": create_checking,
    "401k": create_retirement,
    "MMF": create_mmf
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
            name_list = user_input.strip().split()

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
            char_list = []
            for letter in user_input:
                char_list.append(letter)

            if " " in user_input:
                print("Username cannot contain white space")

            elif len(char_list) < CREDS_MIN or len(char_list) > CREDS_MAX:
                print("Username length requirements not met")

            else:
                return user_input

    if validation_type == "main_menu_key":
        # setting bool here so that loop won't continue to run after breaking
        # out of for look inside while loop after dict function runs.
        need_input = True
        while need_input:
            user_input = input().lower()

            # you're using an int counter for this and incrementing becuase once the
            # methods from the dict run, the error message always runs once the
            # dect method is over. This keeps it from running, when the program
            # returns and goes back to main.
            i = 0
            counter = len(MAIN_MENU_DICT)
            # check to match menu items with user input
            for key, value in MAIN_MENU_DICT.items():
                i += 1
                if i == counter:
                    # if what user types doesn't match anything in menu
                    print("Type an option on the menu")
                if user_input == key.lower():
                    value()
                    need_input = False
                    break

    if validation_type == "password":
        while 1:
            user_input = getpass.getpass()
            if " " in user_input:
                print("No spaces allowed...")
            elif len(user_input) < CREDS_MIN or len(user_input) > CREDS_MAX:
                print("Length requirement not met")
            else:
                return user_input

def customer_exists(customer_name):
    """determines by name if customer exists already

    Returns:
        bool: true/false depending on if customer exists
    """
    customer_list = using_pickle_file("read")
    if customer_list is not None:
        if len(customer_list) != 0:
            for customer in customer_list:
                if customer.name == customer_name:
                    return True

    return False

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

def using_main_menu():
    """will bring you back to the main menu and wait for user input"""

    # display main menu dict items
    print("You can type any menu item\n")
    print_main_menu_dict()

    # let user choose option on main menu
    get_valid_input("main_menu_key")

def print_main_menu_dict():
    """prints all keys in main menu dictionary"""
    for key in MAIN_MENU_DICT:
        print(key)

def main():
    """main entrypoint into program"""
    # set hot key to exit program at any time
    keyboard.add_word_listener("compv", using_main_menu())

    # pyfiglet usage: will dispaly banner for program
    print(BANK_BANNER)
    print("\nWelcome to Vought Banking!")

    # program will not exit until user types exit or manually ends program
    while 1:
        using_main_menu()


if __name__ == "__main__":
    #avoid ctrl C / ctr D error
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        pass
