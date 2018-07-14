#!/usr/bin/env python
# coding=utf-8
import re
import sys

agr = []


# 计算起始子key
def get_agr():
    global agr
    if len(sys.argv) == 2:
        # 单个数字
        pattern1 = "^[0-9]$"
        regex1 = re.compile(r'' + pattern1)
        match1 = regex1.match(sys.argv[1])
        if match1:
            agr.append(sys.argv[1])
            return agr
        #
        # 多级数字必须以数字结尾
        pattern2 = "^([0-9]\.){1,}[0-9]$"
        regex2 = re.compile(r'' + pattern2)
        match2 = regex2.match(sys.argv[1])
        if match2:
            agr.extend(sys.argv[1].split("."))
            return agr
    return agr


# 每级
def match_key(folder):
    if len(agr) == 0:
        correct = 0
        return correct
    pattern = "^" + agr[0] + "$"
    regex = re.compile(r'' + pattern)
    match = regex.match(folder)
    if match:
        correct = len(agr)
        agr.remove(folder)
    else:
        correct = 0
    return correct


def get_key():
    if len(agr) == 0:
        return ""
    folder = agr[0]
    agr.remove(folder)
    return folder