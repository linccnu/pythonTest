"""
Note: This file is the utils script, contain some tiny but useful function.
      You can use them by import the package
"""

import sys

def check_py_version(lowest_requred_version = (3, 5)):
    """
    Note: check the python version, which must not less then the lowest required version.
    :param lowest_requred_version: the lowest required version
    :return: None
    """

    if sys.version_info >= lowest_requred_version:
        pass
    else:
        print('The local python version {}.{}.{} is less than required version {}'.format(
            sys.version_info[0], sys.version_info[1], sys.version_info[2], lowest_requred_version))
        raise RuntimeError('The python version is low than {}'.format(lowest_requred_version))