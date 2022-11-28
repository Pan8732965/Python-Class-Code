# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:54:57 2022

@author: 潘驄杰
作業名稱：坪數轉平方公尺轉換器
"""
print("坪數轉平方公尺轉換器\n")
levelGround = float(input("請輸入欲轉換之坪數："))
squareMeter = int(levelGround)*3.3058
print(str(levelGround)+" 坪為 "+str(squareMeter)+" 平方公尺")