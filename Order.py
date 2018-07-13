#!/usr/bin/env python
# coding=utf-8
import os
import re

# 单个数字 or 多级数字必须以数字结尾
pattern = '^[0-9]$'
path = ""
name = ""
sequence = ""


# 打印序号
def get_sequence(root):
    global sequence
    regex = get_pattern()
    levels = root.split("/")
    for index in range(len(levels)):
        each = levels[index]
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
    global name
    global sequence
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


# pattern
def get_pattern():
    global pattern
    regex = re.compile(r'' + pattern)
    return regex


#
def __main__():
    regex = get_pattern()
    cwd = os.getcwd()
    for root, dirs, files in os.walk(cwd):
        for each in dirs:
            # 匹配每个文件夹
            match = regex.match(each)
            if match:
                target = match.group(0)
                get_alias(root, target)


__main__()
