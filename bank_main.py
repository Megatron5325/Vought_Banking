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
from customer import Customer

# constants
BANK_BANNER = pyfiglet.figlet_format("Vought Banking")

# dictionary use
def go_to_main():
    """will take customer back to main menu"""

def exit_program():
    """exits program"""
    exit()

def view_accounts():
    """displays accounts for current user"""

MAIN_MENU_DICT = {
    "Main": go_to_main,
    "Exit": exit_program,
    "View Accounts": view_accounts

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
            elif user_input.lower in ["n", "no"]:
                return False
            else:
                print("...Enter yes or no...")

def create_new_customer():
    """will create new customer object

    Returns:
        Customer: new customer
    """
    # instansiate Customer class
    customer = Customer()


    return customer

def main():
    """main entrypoint into progam"""

    # pyfiglet usage: will dispaly banner for program
    print(BANK_BANNER)
    print("\nWelcome to Vought Banking!\n" \
        "are you an existing customer?\n" \
            "type Y/N")

    # determine if customer exists
    existing_user = get_valid_input("bool")

    # create new customer or fetch customers existing info
    if existing_user:
        pass
    else:
        # create a new customer
        print("Lets get you started")
        customer = create_new_customer()

if __name__ == "__main__":
    #avoid ctrl C / ctr D error
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        pass
