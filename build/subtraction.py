# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 14:44:09 2021

@author: aanand2
"""


def sub_nums(num1: float, num2: float):
    """
    Function to subtract two numbers.

    Parameters
    ----------
    num1 : int
        First number.
    num2 : int
        Second Number.

    Returns
    -------

    Difference of two number. In-case of error "Invalid Input"

    """
    if isinstance(num1, (int, float)) & isinstance(num2, (int, float)):
        result = num1 - num2
        return result
    return "Invalid Input"
