'''
Programmer: Megan Schleicher
Date: 11/27/2023
Description: a validation class
'''

import getpass
from customer import Customer
from file_reader import File
from bank import Bank

# constants
MIN_NAME_LENGTH = 2
CREDS_MIN = 6
CREDS_MAX = 10

class Validate:
    '''class will take validation type and continuously get
    input from user until correct'''

    @staticmethod
    def get_valid_input(validation_type, main_menu_dict = ()):
        '''will take validation type and get correct input from user'''

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

        if validation_type == "menu_keys":
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
                counter = len(main_menu_dict)
                # check to match menu items with user input
                for key, value in main_menu_dict.items():
                    i += 1
                    if user_input == key.lower():
                        value()
                        need_input = False
                        break

                if i == counter and need_input is True:
                    # if what user types doesn't match anything in menu
                    Bank.print_and_clear_screen(main_menu_dict)
                    print("\nType an option on the menu")

        if validation_type == "password":
            while 1:
                user_input = getpass.getpass()
                if " " in user_input:
                    print("No spaces allowed...")
                elif len(user_input) < CREDS_MIN or len(user_input) > CREDS_MAX:
                    print("Length requirement not met")
                else:
                    return user_input

    @staticmethod
    def customer_exists(customer_name, file_path):
        """determines by name if customer exists already

        Returns:
            bool: true/false depending on if customer exists
        """
        customer_list = File.using_pickle_file("read", file_path)
        if customer_list is not None:
            if len(customer_list) != 0:
                for customer in customer_list:
                    if customer.name == customer_name:
                        return True

        return False

    @staticmethod
    def check_creds(creds, file_path):
        """will take username and password from user and check if user exists"""

        customer = Customer()
        list_of_customers = File.using_pickle_file("read", file_path)

        # check if username and passwrod match any existing customers
        for customer in list_of_customers:
            if customer.username == creds[0]:
                if customer.password == creds[1]:
                    return True
            return False
