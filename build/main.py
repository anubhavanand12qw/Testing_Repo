# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:01:12 2021

@author: aanand2
"""


def add_nums(num1: float, num2: float):
    """
    Function to add two numbers.

    Parameters
    ----------
    num1 : int
        First number.
    num2 : int
        Second Nnumber.

    Returns
    -------

    Sum of two number. In-case of error "Invalid Input"

    """
    if isinstance(num1, (int, float)) & isinstance(num2, (int, float)):
        result = num1 + num2
        return result
    return "Invalid Input"


def main():
    """
    Main function

    Returns
    -------
    None

    """
    try:
        print(add_nums(0, 0))
    except TypeError as excp:
        print(excp)


if __name__ == "__main__":
    main()
