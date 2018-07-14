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


# 定位序号
def locate_key():
    root = os.getcwd()
    dirs = os.listdir(root)
    for each in dirs:
        # 匹配当前目录下每个文件夹
        match = Arg.match_key(each)
        if match > 0:
            step_in_key(root, each)
            print(os.getcwd())
            return


# 访问
def step_in(root, target):
    step_in_key(root, target)


# 访问key
def step_in_key(root, target):
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
            # 删除一级参数
            Arg.rm_arg()


def init():
    array = Arg.get_arg()
    if len(array) == 0:
        print(os.getcwd())
        return
    while len(array):
        locate_key()


#
if __name__ == "__main__":
    # 切换
    init()
