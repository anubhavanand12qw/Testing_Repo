# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:04:49 2021

@author: aanand2
"""

import unittest
import addition


class TestMain(unittest.TestCase):
    """
    Test Class
    """

    def test_add(self):
        """
        Function to test add function in main file

        Returns
        -------
        None.

        """
        #### Sum of positive numbers
        result = addition.add_nums(10, 20)
        self.assertEqual(result, 30)

        result = addition.add_nums("2", 20)
        self.assertEqual(result, "Invalid Input")
        
        result = addition.add_nums([324,435,56,453], [324,435,56,67,34])
        self.assertEqual(result, "Invalid Input")

        result = addition.add_nums("2", "2")
        self.assertEqual(result, "Invalid Input")

    def test_mul(self):
        """
        Function to test add function in main file

        Returns
        -------
        None.

        """
        #### Sum of positive numbers
        result = addition.mul_nums(10, 20)
        self.assertEqual(result, 200)

        result = addition.mul_nums("2", 20)
        self.assertEqual(result, "Invalid Input")

        result = addition.mul_nums("2", "2")
        self.assertEqual(result, "Invalid Input")

    def test_div(self):
        """
        Function to test add function in main file

        Returns
        -------
        None.

        """
        #### Sum of positive numbers
        result = addition.div_nums(20, 20)
        self.assertEqual(result, 1)

        result = addition.div_nums(30, 0)
        self.assertEqual(result, "ZeroDivisionError")

        result = addition.div_nums("2", 20)
        self.assertEqual(result, "Invalid Input")

        result = addition.div_nums("2", "2")
        self.assertEqual(result, "Invalid Input")


if __name__ == "__main__":
    unittest.main()
