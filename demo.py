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

    current_work_dir = os.getcwd()
    print('current work dir:%s' % (current_work_dir))

    # print(os.path.realpath(__file__))
    root_dir = os.path.dirname(os.path.realpath(__file__))
    print('root dir:%s' % (root_dir))
    lib_dir = os.path.join(root_dir, 'lib')
    sys.path.append(lib_dir)
    # print(sys.path)

    lowest_requred_version = (3, 4)
    utils.check_py_version(lowest_requred_version)

    file_list = utils.get_file_list(root_dir)
    for file in file_list:
        file_path = os.path.join(root_dir, file)
        # print('file:%-20s size:%-5d byte' % (file, os.path.getsize(file_path)))       # file size is byte
        print('file:{:<20s} size:{:<5d} byte'.format(file, os.path.getsize(file_path)))

if __name__ == '__main__':
    main()