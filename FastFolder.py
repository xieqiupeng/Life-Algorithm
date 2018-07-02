#!/usr/bin/env python
import os
import sys
import re

if __name__ == '__main__':
    abs = os.path.abspath(__file__)
    real = os.path.realpath(__file__)
    dirname = os.path.dirname(real)
    cwd = os.getcwd()
    print "\n\t" + abs + "\n\t" + real + "\n\t" + dirname + "\n\t" + cwd
    list = os.listdir(dirname)
    pattern = re.compile(r'^[0-9]$|([0-9]\.){1,}[0-9]')
    for folder in list:
        if not os.path.isdir(folder):
            continue
        print folder
        match = pattern.match(folder)
        if match:
            root = match.group(0)
            os.chdir(root)
            childFolder = os.path.dirname(os.path.realpath(__file__))
            print(os.listdir(childFolder))
            os.chdir('..')
        else:
            continue
