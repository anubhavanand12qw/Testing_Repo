# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 15:08:22 2021

@author: aanand2
"""

import unittest
import subtraction


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
        result = subtraction.sub_nums(10, 20)
        self.assertEqual(result, -10)

        result = subtraction.sub_nums("2", 20)
        self.assertEqual(result, "Invalid Input")

        result = subtraction.sub_nums("2", "2")
        self.assertEqual(result, "Invalid Input")


if __name__ == "__main__":
    unittest.main()
