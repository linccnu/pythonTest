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

def check_dir(dir):
    """
    Note: check the path/directory, if not exist, create a new one.
    :param dir: the directory you want to check
    :return: none
    """

    if not os.path.exists(dir):
        os.makedirs(dir)

def check_file(file_path):
    """
    Note: check the specific path is a file, not a directory.
    :param file_path: file path
    :return: True or False
    """

    if os.path.isfile(file_path):
        return True
    else:
        return False

# file extension name
extension_filename = ['txt', 'jpg', 'json', 'cpp', 'c', 'h', 'hpp', 'py']
def shutil_copy_file(source_file_path, dest_file_path):
    """
    Note: copy source file to dest
    :param source_file_path: file source path, can not be directory
    :param dest_file_path: file destination path can be derectory or not.
    :return: None
    """
    import shutil

    if os.path.isfile(source_file_path):
        if os.path.isdir(dest_file_path):
            print("dest is a directory.")
            shutil.copy(source_file_path, dest_file_path)
        elif os.path.isfile(dest_file_path):
            print("dest is a file.")
            shutil.copyfile(source_file_path, dest_file_path)
    else:
        raise RuntimeError("source file {} is not exist.".format(source_file_path))


def contruct_xml_file(file_path = '/home/zhonglin/result.xml'):
    """
    Note: contruct xml file from scratch.
    :param file_path: path of xml file to be saved.
    :return:None
    """

    from xml.etree import ElementTree as ET


    root = ET.Element('annotation')
    folder_name = ET.SubElement(root, 'folder')
    folder_name.text = 'VOC2017'
    file_name = ET.SubElement(root, 'filename')
    file_name.text = 'Sunshine'
    size_name = ET.SubElement(root, 'size')
    width = ET.SubElement(size_name, 'width')
    width.text = '1920'
    height = ET.SubElement(size_name, 'height')
    height.text = '1080'
    depth = ET.SubElement(size_name, 'depth')
    depth.text = '3'
    object = ET.SubElement(root, 'object')

    cls_name = ET.SubElement(object, 'cls_name')
    cls_name.text = 'cat'

    bnbox = ET.SubElement(object, 'bnbox')
    bnbox_xmin = ET.SubElement(bnbox, 'xmin')
    bnbox_xmin.text = '99'
    bnbox_ymin = ET.SubElement(bnbox, 'ymin')
    bnbox_ymin.text = '358'
    bnbox_xmax = ET.SubElement(bnbox, 'xmax')
    bnbox_xmax.text = '135'
    bnbox_ymax = ET.SubElement(bnbox, 'ymax')
    bnbox_ymax.text = '375'

    # another object info
    object = ET.SubElement(root, 'object')
    cls_name = ET.SubElement(object, 'cls_name')
    cls_name.text = 'pedestrian'

    bnbox = ET.SubElement(object, 'bnbox')
    bnbox_xmin = ET.SubElement(bnbox, 'xmin')
    bnbox_xmin.text = '99'
    bnbox_ymin = ET.SubElement(bnbox, 'ymin')
    bnbox_ymin.text = '358'
    bnbox_xmax = ET.SubElement(bnbox, 'xmax')
    bnbox_xmax.text = '135'
    bnbox_ymax = ET.SubElement(bnbox, 'ymax')
    bnbox_ymax.text = '375'

    # convert to string and save it in pretty xml format.
    xml = ET.tostring(root, encoding="UTF-8", method="xml")
    from xml.dom import minidom
    tree = minidom.parseString(xml)
    xml_tree = tree.toprettyxml()
    dom_string = '\n'.join(s for s in xml_tree.splitlines())

    with open(file_path, 'w') as f:
        f.write(dom_string)
    print(xml)

    ## You can also use the following code to generate xml file.
    # from lxml.etree import Element
    # from lxml.etree import SubElement
    # from lxml.etree import tostring
    # root = Element('annotation')
    # folder_name = SubElement(root, 'folder')
    # folder_name.text = 'VOC2017'
    # xml = tostring(root, encoding="UTF-8", method="xml", xml_declaration=True)
    # from xml.dom.minidom import parseString
    # dom = parseString(xml)
    # print(type(dom))
    # with open("result.xml", 'w') as f:
    #     f.write(dom.toprettyxml())
    # print(xml)


def parse_xml_file(file_path):
    """
    Note: parse xml file info, and store them into a dict
    :param file_path: xml file path
    :return: dict. eg {'image_name':xxx, 'size':xxx}
    """
    from xml.etree import ElementTree as ET

    result = dict()

    root = ET.parse(file_path)
    folder_name = root.find('folder').text
    result['folder_name'] = folder_name
    file_name = root.find('filename').text
    result['file_name'] = file_name
    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)
    depth = int(size.find('depth').text)
    result['size'] = [width, height, depth]

    objects = root.findall('object')
    result['object'] = []
    for obj in objects:
        obj_tmp = dict()

        cls_name =obj.find('cls_name').text
        obj_tmp['cls_name'] = cls_name

        bnbox = obj.find('bnbox')
        # You can use the following code to replace
        xmin, ymin, xmax, ymax = map(int, [xx.text for xx in bnbox])

        # xmin = int(bnbox.find('xmin').text)
        # ymin = int(bnbox.find('ymin').text)
        # xmax = int(bnbox.find('xmax').text)
        # ymax = int(bnbox.find('ymax').text)

        obj_tmp['bnbox'] = [xmin,ymin,xmax,ymax]
        result['object'].append(obj_tmp)

    # print(result)
    return result