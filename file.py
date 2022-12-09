import random
import os

file = open("write.txt","w")

for i in range(1,11): #Create numbers
    n = random.randint(1,99)
    file.write(str(n)+"\n")
    print(n)
 
with open("write.txt","r") as process: # To make the numbers load in the nums list.
    content = process.readline()
    nums=[]
    for line in content: # nums的數字加不進去
        line = line.split()
        nums.append(line)

    nums.sort()
    print(nums)
    Max = str(max(nums))
    Min = str(min(nums))
    Average = str(sum(nums) / 10)

with open("write.txt","w") as outfile:
    #outfile.write(str(nums))
    outfile.write(str(nums)+"\n")
    outfile.write("max:"+Max)
    outfile.write("min:"+Min)
    outfile.write("average:"+Average)

print("---")
print(max(nums))
print(min(nums))
print("average: ",sum(nums)/10)