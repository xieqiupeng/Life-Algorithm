#!/usr/bin/env python
# coding=utf-8
import re
import sys

param = []
sequence = []


# 计算序号
def get_sequence():
    global sequence
    global param
    if len(sys.argv) == 2:
        # 单个数字
        pattern1 = "^[0-9]$"
        regex1 = re.compile(r'' + pattern1)
        match1 = regex1.match(sys.argv[1])
        if match1:
            sequence.append(sys.argv[1])
            return sequence
        #
        # 多级数字必须以数字结尾
        pattern2 = "^([0-9]\.){1,}[0-9]$"
        regex2 = re.compile(r'' + pattern2)
        match2 = regex2.match(sys.argv[1])
        if match2:
            sequence.extend(sys.argv[1].split("."))
            return sequence


# pattern
def get_pattern():
    global param
    if len(sys.argv) == 1:
        # 指定前缀
        # 单个数字
        pattern = "^[0-9]$"
        regex = re.compile(r'' + pattern)
        return regex
    if len(sys.argv) == 2:
        # 单个数字
        pattern1 = "^[0-9]$"
        regex1 = re.compile(r'' + pattern1)
        match1 = regex1.match(sys.argv[1])
        #
        # 多级数字必须以数字结尾
        pattern2 = "^([0-9]\.){1,}[0-9]$"
        regex2 = re.compile(r'' + pattern2)
        match2 = regex2.match(sys.argv[1])
        if match1:
            pattern1 = "^" + sys.argv[1] + "$"
            regex1 = re.compile(r'' + pattern1)
            return regex1
        if match2:
            param = sys.argv[1].split(".")
            print(param)
            pattern2 = "^" + param[0] + "$"
            regex2 = re.compile(r'' + pattern2)
            return regex2


# 每级
def folder_match(index):
    pattern = "^" + param[index] + "$"
    regex = re.compile(r'' + pattern)
    return regex
