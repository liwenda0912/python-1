import numpy as np

a = np.array([[1, 2], [3, 4]])
print('第一个数组：')
print(a)
b = np.array([[5, 6], [7, 8]])
print('第二个数组：')
print(b)
print('水平堆叠：')
c = np.hstack((a, b))
print(c)