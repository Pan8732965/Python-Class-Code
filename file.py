# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import os

file = open("write.txt","w")
nums=[]

for i in range(1,11):
    n = random.randint(1,99)
    file.write(str(n)+"\n")
    print(n)
 
# file.close()
with open(p,"r") as infile:
    content = file.readlines()
    #read = file.readlines()
    for line in content:
    nums.append(int(line))
    
print(nums)

nums.sort()

print(max(nums))
print(min(nums))
print("average: ",sum(nums)/10)


file.write(str(nums)+"\n")
file.write("max:",max(nums))
file.write("min:",min(nums))
file.write("average:",sum(nums)/10)

file.close()
#"""


