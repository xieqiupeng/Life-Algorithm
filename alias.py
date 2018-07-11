#!/usr/bin/env python
#coding=utf-8
import os
import sys
import re

# 单个数字 or 多级数字必须以数字结尾
pattern = '^[0-9]$|^([0-9]\.){1,}[0-9]$'
path = ""
name = ""


# 打印仓库列表
def get_list(root, target):
    print(root + "/" + target)
    os.chdir(root)
    os.chdir(target)
    dirs = os.listdir(os.getcwd())
    for each in dirs:
        if os.path.isdir(each):
            print(target + "_" + each)


# 打印alias命令
def get_alias(root, target):
    global path
    global name
    os.chdir(root)
    os.chdir(target)
    path = "ln -s " + root + "/" + target + "/"
    name = target + "_"
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


# Breadth-First-Search
def bfs(dirs):
    for each in dirs:
        if os.path.isdir(each):
            shell = "ln -s " + root + "/" + target + "/" + each + " " + target + "_" + each
            print(shell)


# pattern
def get_pattern():
    global pattern
    if len(sys.argv) == 1:
        # 指定长度
        sys.argv.append("3")
    pattern = "(\.[0-9]){0," + sys.argv[1] + "}$"
    if len(sys.argv) == 2:
        # 指定前缀
        sys.argv.append("[0-9]")
    pattern = "^" + sys.argv[2] + pattern
    regex = re.compile(r'' + pattern)
    return regex


#
def __main__():
    regex = get_pattern()
    if len(sys.argv) == 3:
        sys.argv.append("getAlias")
    cwd = os.getcwd()
    for root, dirs, files in os.walk(cwd):
        for each in dirs:
            match = regex.match(each)
            if match:
                target = match.group(0)
                if sys.argv[3] == "getAlias":
                    get_alias(root, target)
                    continue
                if sys.argv[3] == "getList":
                    get_list(root, target)
                    continue
                else:
                    get_alias(root, target)
                    continue


__main__()
