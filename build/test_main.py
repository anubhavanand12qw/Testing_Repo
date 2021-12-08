# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:04:49 2021

@author: aanand2
"""

import unittest
import main


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
        result = main.add_nums(10, 20)
        self.assertEqual(result, 30)
        
if __name__ == "__main__":
    unittest.main()
        