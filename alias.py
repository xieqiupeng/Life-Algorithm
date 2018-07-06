#!/usr/bin/env python
#coding=utf-8
import os
import sys
import re

# 单个数字 or 多级数字必须以数字结尾

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
    os.chdir(root)
    os.chdir(target)
    dirs = os.listdir(os.getcwd())
    for each in dirs:
        if os.path.isdir(each):
            shell = "ln -s " + root + "/" + target + "/" + each + " " + target + "_" + each
            print shell

#
def __main__():
    if len(sys.argv) == 1:
        sys.argv.append("2")
    pattern = re.compile(r'^[0-9]$|^([0-9]\.){1,' + sys.argv[1] + '}[0-9]$')
    if len(sys.argv) == 2:
        sys.argv.append("getAlias")
    cwd = os.getcwd();
    for root, dirs, files in os.walk(cwd):
        for each in dirs:
            match = pattern.match(each)
            if match:
                target = match.group(0)
                if sys.argv[2] == "getAlias":
                    getAlias(root, target)
                    continue
                if sys.argv[2] == "getList":
                    getList(root, target)
                    continue
                else:
                    getAlias(root, target)
                    continue

__main__()
