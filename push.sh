#!/usr/bin/env bash
# 自动同步脚本

# fetch all
# git remote show origin
# git fetch https://github.com/xieqiupeng/Life-Algorithm master

# push all
export ROOT=/Users/Cobb/Documents/Life-Algorithm
cd $ROOT
git push origin
cd $ROOT/0_Product-Algorithm
git push origin

cd $ROOT/1_Algorithm-Me
git push origin
cd $ROOT/1_Algorithm-Me/1.1_Aim-Chain
git push origin
cd $ROOT/1_Algorithm-Me/1.2_Money-Flow
git push origin
cd $ROOT/1_Algorithm-Me/1.3_Daily-Life
git push origin

cd $ROOT/2_Customer-Profile
git push origin
cd $ROOT/2_Customer-Profile/2.1_Career
git push origin
cd $ROOT/2_Customer-Profile/2.2_My-Dear-Girl
git push origin
cd $ROOT/2_Customer-Profile/2.3_Relationship
git push origin

cd $ROOT/3_Product-Me
git push origin
cd $ROOT/3_Product-Me/3.1_Workout
git push origin
cd $ROOT/3_Product-Me/3.2_Conversation
git push origin

cd $ROOT/4_Scene
git push origin
cd $ROOT/Concealment
git push origin
cd $ROOT/Do-Things
git push origin
cd $ROOT/Technology-and-Expertise
git push origin
cd $ROOT/Knowledge-Book
git push origin
cd $ROOT
