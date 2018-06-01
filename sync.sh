#!/usr/bin/env bash
#! 自动同步脚本

### 全部仓库
# 0_Product-Algorithm
#
# 1_Algorithm-Me
# 1.1_Aim-Chain
# 1.2_Money-Flow
# 1.3_Daily-Life
#
# 2_Customer-Profile
# 2.1_Career
# 2.2_My-Dear-Girl
# 2.3_Relationship
#
# 3_Product-Me
# 3.0.0_Workout
#
# Concealment
# Do-Things
# Knowledge-Book
# Technology-and-Expertise

# fetch all
# git remote show origin
# git fetch https://github.com/xieqiupeng/Life-Algorithm master

# pull all
PATH=/Users/Cobb/Documents/Life-Algorithm
cd $PATH/0_Product-Algorithm
git pull origin
cd $PATH/1_Algorithm-Me
git pull origin
cd $PATH/2_Customer-Profile
git pull origin
