#!/usr/bin/env python
# coding=utf-8
import os
import sys
import re

# 单个数字 or 多级数字必须以数字结尾
pattern = '^[0-9]$'
path = ""
name = ""


# 打印序号
def get_sequence(root):
    regex = get_pattern()
    sequence = ""
    levels = root.split("/")
    for index in range(len(levels)):
        each = levels[index]
        print(str(each))
        match = regex.match(each)
        # if match:
        #     relative = match.group(0)
        #     if sequence == "":
        #         sequence = relative
        #     if sequence != "":
        #         sequence = sequence + "." + relative
        #     return sequence


# 打印alias命令
def get_alias(root, target):
    global path
    global name
    os.chdir(root)
    os.chdir(target)
    path = "ln -s " + root + "/" + target + "/"
    name = get_sequence(root) + "_"
    dirs = os.listdir(os.getcwd())
    dfs(dirs)


# Depth-First-Search
def dfs(dirs):
    global path
    global name
    for index in range(len(dirs)):
        each = dirs[index]
        if os.path.isdir(each):
            path += each
            name = name + each
            shell = path + " " + name
            print(shell)
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
            match = regex.match(each)
            if match:
                target = match.group(0)
                get_alias(root, target)


__main__()
