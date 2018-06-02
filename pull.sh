#!/usr/bin/env bash
# 自动同步脚本

# fetch all
# git remote show origin
# git fetch https://github.com/xieqiupeng/Life-Algorithm master

# pull all
export ROOT=/Users/Cobb/Documents/Life-Algorithm
cd $ROOT
git pull origin
cd $ROOT/0_Product-Algorithm
git pull origin

cd $ROOT/1_Algorithm-Me
git pull origin
cd $ROOT/1_Algorithm-Me/1.1_Aim-Chain
git pull origin
cd $ROOT/1_Algorithm-Me/1.2_Money-Flow
git pull origin
cd $ROOT/1_Algorithm-Me/1.3_Daily-Life
git pull origin

cd $ROOT/2_Customer-Profile
git pull origin
cd $ROOT/2_Customer-Profile/2.1_Career
git pull origin
cd $ROOT/2_Customer-Profile/2.2_My-Dear-Girl
git pull origin
cd $ROOT/2_Customer-Profile/2.3_Relationship
git pull origin

cd $ROOT/3_Product-Me
git pull origin
cd $ROOT/3_Product-Me/3.1_Workout
git pull origin
cd $ROOT/3_Product-Me/3.2_Conversation
git pull origin

cd $ROOT/4_Scene
git pull origin
cd $ROOT/Concealment
git pull origin
cd $ROOT/Do-Things
git pull origin
cd $ROOT/Technology-and-Expertise
git pull origin
cd $ROOT/Knowledge-Book
git pull origin
cd $ROOT
 
