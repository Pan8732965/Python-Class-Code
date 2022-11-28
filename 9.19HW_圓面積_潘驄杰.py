# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 10:35:02 2022

@author: User
"""
"""
 作業上傳時間：2022/9/19
 名字: 潘驄杰
 學號: 11144209
 此程式為不斷可以繼續詢問的然後計算的循環機制，省去每次執行要按開始鍵的麻煩，加上對於小數點轉成整數去做優化。
"""
def Calc(): #函式概括計算過程
    enterValue = input('請輸入想要計算圓球體積之半徑：') 
    IntEnterValue = int(enterValue) #輸入值由float轉int
    CalcValue = (4/3)*3.14*IntEnterValue*IntEnterValue*IntEnterValue
    OutputValue = int(CalcValue) #輸出值由float轉int
    print("半徑為",enterValue,"的球體積約為",OutputValue,"\n---")

Calc() #開始時之計算

while input("還要繼續嗎? [y/n]：") == "y": #重複迴圈詢問答覆
    print("---")
    Calc()
