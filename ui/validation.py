# ***************************************************************
# Author: Armaghan Qadiry
# Lab : 3
# File: input_validation.py
# Description: Contains input validation functions for user input.
# ***************************************************************

def get_string(prompt="Please select an item: "):
    """
    :param prompt: Prompt to select an item.
    :return: string
    """
    while True:
        chars = input(prompt).strip()
        if chars != "":
            return chars
        else:
            print("Invalid option. Please try again.")


def get_valid_year(prompt):
    """
    Prompt the user for a valid year between 1880 and 2025.
    Ensures input is a number within the range.
    """
    while True:
        try:
            year = int(input(prompt))
            if 1880 <= year <= 2025:
                return year
            print("Please enter a valid year between 1880 and 2025.")
        except ValueError:
            print("Invalid input. Please enter a number.")
