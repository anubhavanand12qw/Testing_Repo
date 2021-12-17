# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 14:42:20 2021

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
        Second Number.

    Returns
    -------

    Sum of two number. In-case of error "Invalid Input"

    """
    if isinstance(num1, (int, float)) & isinstance(num2, (int, float)):
        result = num1 + num2
        return result
    return "Invalid Input"


def mul_nums(num1: float, num2: float):
    """
    Function to multiply two numbers.

    Parameters
    ----------
    num1 : int
        First number.
    num2 : int
        Second Number.

    Returns
    -------

    Multiplication of two number. In-case of error "Invalid Input"

    """
    if isinstance(num1, (int, float)) & isinstance(num2, (int, float)):
        result = num1 * num2
        return result
    return "Invalid Input"


def div_nums(num1: float, num2: float):
    """
    Function to divide two numbers.

    Parameters
    ----------
    num1 : int
        First number.
    num2 : int
        Second Number.

    Returns
    -------

    Division of two number. In-case of error "Invalid Input"

    """
    if isinstance(num1, (int, float)) & isinstance(num2, (int, float)):
        if num2 == 0:
            return "ZeroDivisionError"
        result = num1 / num2
        return result
    return "Invalid Input"
