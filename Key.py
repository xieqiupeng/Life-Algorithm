#!/usr/bin/env python
# coding=utf-8
import re
import sys

key = []


# 计算起始子key
def get_key_array():
    global key
    if len(sys.argv) == 2:
        # 单个数字
        pattern1 = "^[0-9]$"
        regex1 = re.compile(r'' + pattern1)
        match1 = regex1.match(sys.argv[1])
        if match1:
            key.append(sys.argv[1])
            return key
        #
        # 多级数字必须以数字结尾
        pattern2 = "^([0-9]\.){1,}[0-9]$"
        regex2 = re.compile(r'' + pattern2)
        match2 = regex2.match(sys.argv[1])
        if match2:
            key.extend(sys.argv[1].split("."))
            return key
    return key


# 每级
def match_key(folder):
    if len(key) == 0:
        correct = 0
        return correct
    pattern = "^" + key[0] + "$"
    regex = re.compile(r'' + pattern)
    match = regex.match(folder)
    if match:
        correct = 1
        key.remove(folder)
    else:
        correct = 0
    return correct


# pattern
def match_pattern(name):
    # 指定单个数字前缀
    pattern = "^[0-9]$"
    regex = re.compile(r'' + pattern)
    match = regex.match(name)
    if match:
        return 1
    if not match:
        return 0


def get_pattern():
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
            pattern2 = "^" + param[0] + "$"
            regex2 = re.compile(r'' + pattern2)
            return regex2
