#!/usr/bin/env python
# coding=utf-8
import re
import sys

arg = []


# 计算起始子key
def get_arg():
    global arg
    if len(sys.argv) == 2:
        # 单个数字
        pattern1 = "^[0-9]$"
        regex1 = re.compile(r'' + pattern1)
        match1 = regex1.match(sys.argv[1])
        if match1:
            arg.append(sys.argv[1])
            return arg
        #
        # 多级数字必须以数字结尾
        pattern2 = "^([0-9]\.){1,}[0-9]$"
        regex2 = re.compile(r'' + pattern2)
        match2 = regex2.match(sys.argv[1])
        if match2:
            arg.extend(sys.argv[1].split("."))
            return arg
    return arg


# 每级
def match_key(folder):
    if len(arg) == 0:
        correct = 0
        # print("参数为空")
        return correct
    pattern = "^" + arg[0] + "$"
    regex = re.compile(r'' + pattern)
    match = regex.match(folder)
    if match:
        correct = len(arg)
        # print("参数正确 " + arg[0])
        return correct
    if not match:
        correct = 0
        # print("参数错误 " + folder)
        return correct


def check_arg():
    if len(arg) == 0:
        # print("参数为空")
        return 0
    if not len(arg) == 0:
        # print(arg)
        return arg[0]


def rm_arg():
    print(arg)
    arg.remove(arg[0])

