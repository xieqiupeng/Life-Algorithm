#!/usr/bin/env python
# coding=utf-8
"""
识别
"""
import os
import re
import Key
import Locate
import List


# 根据文件路径计算序号
def get_sequence(root):
    key = ""
    levels = root.split("/")
    for each in levels:
        pattern = "[0-9]"
        regex = re.compile(r'' + pattern)
        match = regex.match(each)
        if not match:
            continue
        if key == "":
            key = each
            continue
        if not key == "":
            key = key + "." + each
            continue
    return key


# 生成别名
def get_alias(root):
    start = "ln -s " + root + " "
  #  start = ""
    sequence = get_sequence(root)
    name = os.path.basename(root)
    shell = start + sequence + "_" + name
    return shell


# 打印所有子目录
def print_list(root):
    # dirs 文件夹
    # files 文件
    for root, dirs, files in os.walk(root):
        for each in dirs:
            # 匹配每个文件夹
            match = Key.match_pattern(each)
            if match:
                List.step_in(root, each)
                print(get_alias(os.getcwd()))
                os.chdir(root)


#
if __name__ == "__main__":
    # 切换
    Locate.init()
    # 所有
    print_list(os.getcwd())
