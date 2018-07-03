#!/usr/bin/env python
#coding=utf-8
import os
import sys
import re

# 单个数字 or 多级数字必须以数字结尾
pattern = re.compile(r'^[0-9]$|^([0-9]\.){1,}[0-9]$')

# 打印文件
def getList():
    cwd = os.getcwd();
    for root, dirs, files in os.walk(cwd):
        for each in dirs:
            match = pattern.match(each)
            if match:
                target = match.group(0)
                # 打印仓库序号
                print root + "/" + target

# 遍历所有序号仓库
def getAlias():
    cwd = os.getcwd();
    for root, dirs, files in os.walk(cwd):
        for each in dirs:
            match = pattern.match(each)
            if match:
                target = match.group(0)
                showChild(root, target)

# 打印仓库正式名称
def showChild( root, target ):
    os.chdir(root)
    os.chdir(target)
    dirs = os.listdir(os.getcwd())
    for each in dirs:
        if os.path.isdir(each):
            shell = "ln -s " + root + "/" + target + "/" + each + " " + target + "_" + each
            print shell
            # print target + "_" + each

#
def __main__():
    if len(sys.argv) == 1:
        return
    if sys.argv[1] == "getAlias":
        getAlias()
    else:
        getList()

__main__()
