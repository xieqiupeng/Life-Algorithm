#!/usr/bin/env python
# coding=utf-8
import os
import sys
import Patter

path = ""
sequence = ""
name = ""
sequence = []


# 计算序号
def get_sequence():
    global sequence
    sequence = Patter.get_sequence()
    print(sequence)
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


# 找到序号文件夹
def find_sub_folder():
    regex = Patter.get_pattern()
    cwd = os.getcwd()
    # dirs 文件夹
    # files 文件
    for root, dirs, files in os.walk(cwd):
        for each in dirs:
            # 匹配每个文件夹
            match = regex.match(each)
            if match:
                target = match.group(0)
                get_alias(root, target)


# 切换到指定序号
def get_alias(root, target):
    global path
    global name
    os.chdir(root)
    os.chdir(target)
    path = "ln -s " + root + "/" + target + "/"
    dirs = os.listdir(root + "/" + target)
    dfs(dirs)


# 打印所有子目录
def dfs(dirs):
    global path
    global sequence
    global name
    # print(dirs)
    # filter()
    for index in range(len(dirs)):
        each = dirs[index]
        if os.path.isdir(each):
            # path += each
            sequence = get_sequence(path)
            name = sequence + "_" + each
            # shell = path + " " + name
            shell = name
            print(shell)
            sequence = ""
            continue
        else:
            continue


#
def __main__():
    regex = Patter.get_pattern()
    cwd = os.getcwd()
    # dirs 文件夹
    # files 文件
    get_sequence()
    # find_sub_folder()


__main__()
