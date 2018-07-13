#!/usr/bin/env python
# coding=utf-8
import os
from Patter import *

path = ""
sequence = ""
name = ""


# 打印序号
def get_sequence(root):
    global sequence
    levels = root.split("/")
    for index in range(len(levels)):
        each = levels[index]
        regex = get_pattern()
        # regex = folder_match(index)
        match = regex.match(each)
        if match:
            relative = match.group(0)
            if sequence == "":
                sequence = relative
                continue
            if sequence != "":
                sequence = sequence + "." + relative
                continue
    return sequence


# 打印alias命令
def get_alias(root, target):
    global path
    global name
    os.chdir(root)
    os.chdir(target)
    path = "ln -s " + root + "/" + target + "/"
    dirs = os.listdir(root + "/" + target)
    dfs(dirs)


# Depth-First-Search
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
    regex = get_pattern()
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


__main__()
