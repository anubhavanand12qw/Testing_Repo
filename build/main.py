# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:01:12 2021

@author: aanand2
"""

import addition
import subtraction


def main():
    """
    Main function

    Returns
    -------
    None

    """
    try:
        print(addition.add_nums(0, 0))
        print(addition.mul_nums(34, 54))
        print(addition.div_nums(34, 54))
        print(subtraction.sub_nums(0, 0))
    except TypeError as excp:
        print(excp)


if __name__ == "__main__":
    main()
