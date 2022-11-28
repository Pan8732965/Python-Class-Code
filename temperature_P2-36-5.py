# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:18:39 2022

@author: 潘驄杰
作業名稱：溫度單位轉換器
"""
Celsius =input("請輸入攝氏溫度 Celsius：") #input thing is string
Fahrenheit = float(Celsius)*1.8+32 # calculate and string  to number(float)
intFahrenheit = int(Fahrenheit) # float to int
print("轉換後的華氏溫度 Fahrenheit： ", intFahrenheit)

