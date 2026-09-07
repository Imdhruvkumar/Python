import numpy as np 

array_1 = np.array([[1,2,3],[4,5,6]])
array_2 = np.random.rand(2,3)
array_3 = np.zeros((4,4))

np.save('array1.npy',array_1)

loaded = np.load('array1.npy')
# print(loaded)