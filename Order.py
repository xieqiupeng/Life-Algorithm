#!/usr/bin/env python
# coding=utf-8
import os
import Patter

path = ""
shell = ""
key = ""


# 计算序号
def get_key():
    global key
    key_list = Patter.get_key()
    if len(key_list) > 0:
        key = ".".join(key_list)
    return key


# 定位序号
def locate_key():
    root = os.getcwd()
    dirs = os.listdir(root)
    for each in dirs:
        # 匹配每个文件夹
        match = Patter.match_key(each)
        if match:
            step_in_key(root, each)


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
            get_alias(root + "/" + each)


# 生成别名
def get_alias(root):
    global path
    global shell
    path = root
    name = os.path.basename(root)
    shell = "ln -s " + path + " " + key + "_" + name
    print(shell)
    # print_list(path)


# 打印所有子目录
def print_list(root):
    global key
    global shell
    #
    # dirs 文件夹
    # files 文件
    for root, dirs, files in os.walk(root):
        for each in dirs:
            # 匹配每个文件夹
            match = Patter.match_pattern(each)
            if match:
                os.chdir(each)
                step_in_key(root, each)
                os.chdir(root)


#
def __main__():
    # 计算序号
    get_key()
    # 定位
    # locate_key()
    # 打印
    print_list(os.getcwd())


__main__()
