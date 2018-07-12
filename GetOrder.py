#!/usr/bin/env python
#coding=utf-8
import os
import sys
import re

# 单个数字 or 多级数字必须以数字结尾
pattern = '^[0-9]$'
path = ""
name = ""
absolute = ""


# 打印绝对序号
def get_absolute(relative):
    global absolute
    if absolute == "":
        absolute = relative
        return absolute
    if absolute != "":
        absolute = absolute + "." + relative
        return absolute


# 打印alias命令
def get_alias(root, target):
    global path
    global name
    os.chdir(root)
    os.chdir(target)
    path = "ln -s " + root + "/" + target + "/"
    name = get_absolute(target) + "_"
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
            # style = "\n"
            style = ""
            shell = path + " " + name + style
            print(shell)
            continue
            # getAlias()
        else:
            continue
            # path = path + each
            # name = name + each


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
