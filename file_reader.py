'''
Programmer: Megan Schleicher
Date 12/9/2023
Version: 1.0
Description: will allow reading/ writing/ executing
any type of file.
'''
import pickle
import os

class File:
    '''will allow reading/writing/executing a file'''

    @staticmethod
    def using_pickle_file(serialization_type = "read", customer = None, file_path = ""):
        """deserializes pickle file to get list of customers gor program"""
        #loop through stored objects in pickle file and store in list or read from list
        pickle_command = 'r+b'

        if serialization_type == "write":
            pickle_command = 'w+b'

        with open(file_path, pickle_command) as file:
            if serialization_type == "read" and os.path.getsize(file_path) > 0:
                #load existing customer info into list
                list_of_file_objects = pickle.load(file)
                return list_of_file_objects

            elif serialization_type == "write":

                # if pickle file has info and you're loading it
                if os.path.getsize(file_path) > 0:
                    # get all existing customers
                    list_of_file_objects = pickle.load(file)
                    # append new customer to list
                    list_of_file_objects.append(customer)

                # if pickle file has no info so you're creating new list
                else:
                    # no customers exist so creat a list for them
                    list_of_file_objects = []
                    # append customer object to list
                    list_of_file_objects.append(customer)

                # store new list in the pickl file
                pickle.dump(list_of_file_objects, file)
                # close file
                file.close()

                return list_of_file_objects
