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
    print("[get_file_list] Test ok.")


    # ROOT_DIR = '/home/zhonglin/workspace/github/pythonTest'
    ROOT_DIR = '/data/workspace/github/pythonTest/'
    # ROOT_DIR = ''
    new_dir = utils.remove_the_slash_in_dir(ROOT_DIR)
    print('new_dir:{}'.format(new_dir))
    print("[remove_the_slash_in_dir] Test ok.")


    test_dir = "/data/python_test"
    utils.check_dir(test_dir)

    source_file_path = "/data/workspace/github/pythonTest/lib/utils.py"
    dest_file_path = "/data/python_test/"
    utils.shutil_copy_file(source_file_path, dest_file_path)
    if os.path.isdir(dest_file_path):
        print(os.listdir(dest_file_path))
    else:
        print(os.listdir(os.path.dirname(dest_file_path)))
    print("[shutil_copy_file] Test ok.")

    # Note:os.path.dirname() usually combine with os.path.abspath(__file__) together when using
    xml_file_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    utils.check_dir(xml_file_dir)
    xml_file_path = os.path.join(xml_file_dir, 'result.xml')
    utils.contruct_xml_file(xml_file_path)
    print("[contruct_xml_file] Test ok.")

    anno_result = utils.parse_xml_file(xml_file_path)
    print(anno_result)
    print("[parse_xml_file] Test ok.")


if __name__ == '__main__':
    main()