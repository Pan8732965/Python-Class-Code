with open("data.txt","r") as infile:
    content = infile.readlines()

print(content)

with open("nums.txt","w") as outfile:
    for i in content:
        print(i.strip()) # strip 清除字母字符
        try:
            if int(i.strip()): #在每列中尋找是"數字"的字符並且只將數字字符列印出來。
                outfile.write(i)
        except:
            pass

print("---")

with open("nums.txt","r") as view:
    printOut = view.readlines()
    ToString = ''.join(printOut)
    print(ToString)