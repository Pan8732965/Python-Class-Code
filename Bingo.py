import random
b = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

for i in range(5):
    for j in range(5):
        print(b[i][j],"\t",end="")
    print()

print("---\n")

for i in range(30): #取亂數，將賓果中的兩個值調換
    i1 = random.randint(0,4)
    j1 = random.randint(0,4)
    i2 = random.randint(0,4)
    j2 = random.randint(0,4)
    t = b[i1][j1]
    b[i1][j1] = b[i2][j2]
    b[i2][j2] = t

print()
for i in range(5):
    for j in range(5):
        print(b[i][j],"\t",end="")
    print()

#---另一個寫法---
print("---\n")

b = [i+1 for i in range(25)]
b2 = []
random.shuffle(b)
for i in range(0,25,5):
        b2.append(b[i:i+5])

for i in range(5):
    for j in range(5):
        print(b2[i][j],"\t",end="")
    print()