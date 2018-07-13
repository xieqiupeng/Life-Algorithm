#!/usr/bin/env python
# coding=utf-8
import os
import Patter

path = ""
name = ""
sequence = []


# 计算序号
def get_sequence():
    global sequence
    sequence = Patter.get_sequence()
    # levels = root.split("/")
    # for index in range(len(levels)):
    #     each = levels[index]
    #
    #     # regex = folder_match(index)
    #     match = regex.match(each)
    #     if match:
    #         relative = match.group(0)
    #         if sequence == "":
    #             sequence = relative
    #             continue
    #         if sequence != "":
    #             sequence = sequence + "." + relative
    #             continue
    return sequence


# 定位文件夹
def location():
    root = os.getcwd()
    dirs = os.listdir(root)
    for each in dirs:
        # 匹配每个文件夹
        match = Patter.match_sequence(each)
        if match:
            relocation(root, each)


# 定位文件夹
def relocation(root, target):
    global path
    global name
    os.chdir(root)
    os.chdir(target)
    path = "ln -s " + root + "/" + target + "/"
    dirs = os.listdir(root + "/" + target)
    print_list(dirs)


# 生成别名
def get_alias(root, target):
    global path
    global name
    os.chdir(root)
    os.chdir(target)
    path = "ln -s " + root + "/" + target + "/"
    dirs = os.listdir(root + "/" + target)
    print_list(dirs)


# 打印所有子目录
def print_list(dirs):
    global path
    global sequence
    global name
    # print(dirs)
    # filter()
    for index in range(len(dirs)):
        each = dirs[index]
        if os.path.isdir(each):
            path += each
            # sequence = get_sequence(path)
            name = each
            shell = path + " " + name
            # shell = name
            print(shell)
            sequence = ""
            continue
        else:
            continue


#
def __main__():
    # 计算序号
    get_sequence()
    # 定位
    location()
    #
    # print_list()


__main__()
