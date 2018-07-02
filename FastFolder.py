#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    abs = os.path.abspath(__file__)
    real = os.path.realpath(__file__)
    dirname = os.path.dirname(real)
    cwd = os.getcwd()
    list = os.listdir(dirname)
    print "\n\t" + abs + "\n\t" + real + "\n\t" + dirname + "\n\t" + cwd
    print list
