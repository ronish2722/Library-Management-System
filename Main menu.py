from library_management_system import display
from library_management_system import borrow
from library_management_system import return_
"""Importing the functions form another module"""


def main_menu():
    """This modules asks the customer of their action"""
    command = 0
    # Layout for main menu
    print("-------------------------------")
    print("For displaying books please enter 1.")
    print("For borrowing books please enter 2.")
    print("For returning books please enter 3.")
    print("For exiting please enter 4.")

    # Until the inputted value is 4 the code keeps running
    while command != 4:
        print("-------------------------------")
        # Exception Handling
        while True:
            try:
                # Asking for command
                command = int(input("Enter as instructed above: "))
                break
            except:
                # If invalid value is entered
                print("-------------------------------")
                print("Enter a valid command")
                print("-------------------------------")

        print("-------------------------------")
        if command == 1:
            # Calling function display
            display()
        elif command == 2:
            # Calling function borrow
            borrow()
        elif command == 3:
            # Calling function return_
            return_()
        elif command == 4:
            # Exiting the program
            print("Thank you!!!!")
            print()
            break
        else:
            # If invalid command is written
            print("Enter a valid command")

# Calling function main_menu
main_menu()
