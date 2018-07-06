#!/usr/bin/env python
#coding=utf-8
import os
import sys
import re

# 单个数字 or 多级数字必须以数字结尾
pattern = re.compile(r'^[0-9]$|^([0-9]\.){1,}[0-9]$')
path = "";
name = "";

# 打印仓库列表
def getList( root, target ):
    print root + "/" + target
    os.chdir(root)
    os.chdir(target)
    dirs = os.listdir(os.getcwd())
    for each in dirs:
        if os.path.isdir(each):
            print target + "_" + each

# 打印alias命令
def getAlias( root, target ):
    global path
    global name
    os.chdir(root)
    os.chdir(target)
    path = "ln -s " + root + "/" + target + "/"
    name = target + "_"
    dirs = os.listdir(os.getcwd())
    dfs( dirs )

# Depth-First-Search
def dfs( dirs ):
    global path
    global name
    for index in range(len(dirs)):
        each = dirs[index]
        if os.path.isdir(each):
            path += each
            name = name + each
            style = "\n"
            # style = ""
            shell = path + " " + name + style
            print shell
            continue
            # getAlias()
        else:
            continue
            # path = path + each
            # name = name + each

# Breadth-First-Search
def bfs( dirs ):
    for each in dirs:
        if os.path.isdir(each):
            shell = "ln -s " + root + "/" + target + "/" + each + " " + target + "_" + each
            print shell

# pattern
def getPattern():
    global pattern
    # 全部显示
    if len(sys.argv) == 1:
        sys.argv.append("")
        str = "^[0-9]$|^([0-9]\.){1," + sys.argv[1] + "}[0-9]$"
    # 指定模版
    if len(sys.argv) == 2:
        sys.argv.append("")
        str = "^" + sys.argv[1] + "(\.[0-9]){0}" + "[0-9]$"
    pattern = re.compile(r''+ str +'')
    # print pattern

#
def __main__():
    getPattern()
    if len(sys.argv) == 3:
        sys.argv.append("getAlias")
    cwd = os.getcwd();
    for root, dirs, files in os.walk(cwd):
        for each in dirs:
            match = pattern.match(each)
            if match:
                target = match.group(0)
                if sys.argv[3] == "getAlias":
                    getAlias(root, target)
                    continue
                if sys.argv[3] == "getList":
                    getList(root, target)
                    continue
                else:
                    getAlias(root, target)
                    continue

__main__()
