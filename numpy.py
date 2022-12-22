import numpy as np
A = np.linspace(1,11,6).reshape(2,3)

print("陣列 A：\n",A) #(1) 印出陣列A

print("陣列 A維度：\n",A.ndim) #(2) 維度
print("陣列 A形狀：\n",A.shape) #(2)形狀
print("陣列 A元素個數：\n",A.size) #(2) 元素個數
print("陣列 A元素大小：\n",A.itemsize) #(2) 元素大小

print("陣列 A最小值：\n",np.min(A)) #(3) 最小值
print("陣列 A最大值：\n",np.max(A)) #(3) 最大值

B = np.transpose(A) #(4) 轉置矩陣
print("轉置矩陣 B：\n",B)

C = A + A #(5) 相加
print("矩陣 C：\n",C)

D = A @ B #(6) 二維陣列相乘
print("D=",D)

E = A*3 #(7) A乘以三
print("E=",E)

Stack = np.vstack((A,E)) #(8)A,E垂直堆疊
print("A,E垂直堆疊:\n",Stack)