#!/usr/bin/env python
#coding=utf-8
import os
import sys
import re

# 遍历所有序号仓库
def cdNextFolder( all ):
    pattern = re.compile(r'^[0-9]$|([0-9]\.){1,}[0-9]')
    for root, dirs, files in os.walk(all):
        for each in dirs:
            match = pattern.match(each)
            if match:
                target = match.group(0)
                print(target)
                # 序号文件夹
                os.chdir(target)
                child = os.getcwd()
                listNextFolder(child)
                os.chdir('..')

# 打印序号名称和仓库名称
def listNextFolder( all ):
    print(all)
    dirs = os.listdir(all)
    for each in dirs:
        if os.path.isdir(each):
            print(each)

if __name__ == '__main__':
    abs = os.path.abspath(__file__)
    real = os.path.realpath(__file__)
    dirname = os.path.dirname(real)
    cwd = os.getcwd()
    print "\n\t" + abs + "\n\t" + real + "\n\t" + dirname + "\n\t" + cwd
    cdNextFolder(cwd)
