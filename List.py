#!/usr/bin/env python
# coding=utf-8
"""
进入序号Value目录
"""
import os
import Arg

path = ""
shell = ""
key = ""


# 定位当前目录下的序号
def list_key(root):
    dirs = os.listdir(root)
    for each in dirs:
        # 匹配当前目录下每个文件夹
        match = Arg.match_key(each)
        if match > 0:
            step_in(root, each)
            return


# 访问key
def step_in(root, target):
    os.chdir(root)
    os.chdir(target)
    step_in_value(root + "/" + target)


# 访问value
def step_in_value(root):
    files = os.listdir(root)
    for each in files:
        if os.path.isdir(each):
            os.chdir(each)
            # 目录切换成功，
            # print(os.getcwd())


def init():
    array = Arg.get_arg()
    if len(array) == 0:
        print(os.getcwd())
        return
    while len(array):
        list_key(os.getcwd())
    print(os.getcwd())


#
if __name__ == "__main__":
    # 切换
    init()
