# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:01:12 2021

@author: aanand2
"""


def add_nums(num1: float, num2: float) -> int:
    """
    Function to add numbers.

    Parameters
    ----------
    num1 : int
        First number.
    num2 : int
        Second Nnumber.

    Returns
    -------
    int
        Sum of both the numbers.

    """
    if isinstance(num1, (int, float)) & isinstance(num2, (int, float)):
        result = num1 + num2
        return result
    return TypeError("Invalid Input")


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
