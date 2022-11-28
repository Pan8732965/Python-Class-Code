import string
import os
file = open("sample.txt","r",encoding="utf-8")
Tolist = file.readlines()
Tostring = ' '.join(Tolist)
countWords = len(Tostring.split())
countRow = len(open("sample.txt","r",encoding="utf-8").readlines())
file_Name = os.path.basename('Python/sample.txt')
print("在",file_Name,"裡的內容：\n",Tostring,"\n---")
print("在",file_Name,"檔案裡共有",countRow,"行",countWords,"個字")
file.close()