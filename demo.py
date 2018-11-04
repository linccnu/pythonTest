"""
Note: This is the practice Demo of python
Written by zhonglin. 2018.11.04
"""

import os
import sys

from lib import utils as utils


def main():
    """
    Note: The main function implementation
    :return:
    """

    ROOT_DIR = os.path.abspath('.')
    LIB_DIR = os.path.join(ROOT_DIR, 'lib')
    sys.path.append(LIB_DIR)
    # print(sys.path)

    lowest_requred_version = (3, 5)
    utils.check_py_version(lowest_requred_version)

if __name__ == '__main__':
    main()