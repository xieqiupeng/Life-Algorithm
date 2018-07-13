#!/usr/bin/env python
# coding=utf-8
import os
import Patter

path = ""
shell = ""
name = ""
sequence = ""


# 计算序号
def get_sequence():
    global sequence
    sequence_list = Patter.get_sequence()
    if len(sequence_list) > 0:
        sequence = ".".join(sequence_list)
    return sequence


# 定位文件夹
def location_sequence():
    root = os.getcwd()
    dirs = os.listdir(root)
    for each in dirs:
        # 匹配每个文件夹
        match = Patter.match_sequence(each)
        if match:
            step_in_sequence(root, each)


# 定位文件夹
def step_in_sequence(root, target):
    os.chdir(root)
    os.chdir(target)
    get_alias(root, target)


# 生成别名
def get_alias(root, target):
    global path
    global shell
    path = root + "/" + target
    shell = "ln -s " + path
    print(shell)


# 打印所有子目录
def print_list(root):
    global sequence
    global name
    global shell
    #
    # dirs 文件夹
    # files 文件
    for root, dirs, files in os.walk(root):
        for each in dirs:
            # 匹配每个文件夹
            match = Patter.match_sequence(each)
            if match:
                each += each
                # sequence = get_sequence(path)
                name = sequence + "_" + each
                shell = shell + " " + name
                # shell = name
                sequence = ""
                continue
            else:
                continue


#
def __main__():
    # 计算序号
    get_sequence()
    # 定位
    location_sequence()


__main__()
