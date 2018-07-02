#!/usr/bin/env python
#coding=utf-8
import os
import sys
import re

def cdNextFolder( root ):
    list = os.listdir(root)
    pattern = re.compile(r'^[0-9]$|([0-9]\.){1,}[0-9]')
    for folder in list:
        if not os.path.isdir(folder):
            continue
            print folder
        match = pattern.match(folder)
        # 找到序号文件夹
        if match:
            target = match.group(0)
            os.chdir(target)
            child = os.getcwd()
            # print(child)
            childList = os.listdir(child)
            # print(childList)
            for each in childList:
                print(each)
                # cdNextFolder( child )
            os.chdir('..')
        else:
            continue

if __name__ == '__main__':
    abs = os.path.abspath(__file__)
    real = os.path.realpath(__file__)
    dirname = os.path.dirname(real)
    cwd = os.getcwd()
    print "\n\t" + abs + "\n\t" + real + "\n\t" + dirname + "\n\t" + cwd
    cdNextFolder(cwd)
