"""
Note: This file is the utils script, contain some tiny but useful function.
      You can use them by import the package
"""

import os
import sys


def check_py_version(lowest_requred_version = (3, 4)):
    """
    Note: check the python version, which must not less then the lowest required version.
    :param lowest_requred_version: the lowest required version
    :return: None
    """

    if sys.version_info >= lowest_requred_version:
        pass
    else:
        raise RuntimeError('The python version {}.{}.{} is low than {}'.format(
            sys.version_info[0], sys.version_info[1], sys.version_info[2], lowest_requred_version))


def get_file_list(file_dir):
    """
    Note: get all the file in the specific dir
    :param file_dir: file directory
    :return: file list
    """

    file_list = os.listdir(file_dir)
    file_list = [file for file in file_list if os.path.isfile(os.path.join(file_dir, file))]

    # you can also use os.walk to recursively list all the files
    # for root, dirs, file_list in os.walk(file_dir)

    return file_list

def remove_the_slash_in_dir(dir):
    """
    Note: remove the last slash in directory.
    :param dir: the absolute directory
    :return: directory without slash in the end
    """

    if dir.endswith('/'):
        return dir[:-1]
    else:
        return dir