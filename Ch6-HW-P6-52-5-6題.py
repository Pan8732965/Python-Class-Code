# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 14:13:01 2022

@author: USER
"""

# HW-5

S1 = {1,8,9,7,6}
S2 = {2,5,6,8,9}

#(1)：S1有5個元素
len(S1)
#(2)：False。S1不是S2的子集合
S1 <= S2
#(3)聯集
S3 = S1.union(S2)
print(S3) # {1, 2, 5, 6, 7, 8, 9}
#(4)交集
S3 = S1.intersection(S2)
print(S3) # {8, 9, 6}
#(5)差集
S3 = S1.difference(S2)
print(S3) # {1, 7}
#(6)S1元素總和 = 31
sum = 0
for i in S1:
    sum += i
print("S1的總和為：",sum)

#---

# HW-6
a = list(input("請輸入一個英文單字："))
a.reverse()
b = len(a)
for i in range(b):
    print(str(a[i]))

