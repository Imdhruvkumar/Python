# =========numpy array and basics==============================

import numpy as np 

#======creating array from list ================================

#--------------------------------------------
arr_1d = np.array([1,2,3,4,5])
# print("1D array",arr_1d)

arr_2d = np.array([[1,2,3],[4,5,6]])
# print("2D array",arr_2d)
#---------------------------------------------

# ==============list vs numpy array=============================

#-----------------------------------------------------
py_list = [1,2,3]
# print("python list multiplicaton",py_list * 2)

np_array = np.array([1,2,3])
# print("numpy array multiplication",np_array * 2) # element wise multiplication 

#---------------------------------------------------

import time 

#-----------------------------------------------------
start = time.time()
py_list = [i*2 for i in range(1000000)]

# print("/n list operation time",time.time()-start)

start1 = time.time()
np_array = np.arange(1000000)*2
# print("/n  numpy array operation time",time.time()-start1)
#------------------------------------------------------

#============creating from scratch========================
#=========== creating matrics============================


#---------------------------------------------
zeros = np.zeros((3,4))
# print("numpy zeros matrics\n" , zeros)

ones = np.ones((3,4))
# print("numpy oness matrics\n" , ones)

# constant number metrics

full = np.full((2,2),7)
# print("numpy full matrics\n" , full)

#random number matrics

random = np.random.random((2,3))
# print("numpy random matrics\n" , random)

sequence = np.arange(0,10,2)
# print("numpy  arange \n" , sequence)

#-----------------------------------------------------

# ============Vecter, matrix and tensor==========================

#----------------------------------------------------

vecter = np.array([1,2,3,4,5,6])
# print("numpy vecter \n" , vecter)


matrix = np.array([[1,2,3],[4,5,6]])
# print("numpy matrix \n" , matrix)


# used for  multi diamention

tensor = np.array([[[1,2,3],[4,5,6]],
                   [[1,2,3],[3,4,5]]])

# print("numpy tensor \n" ,tensor)

#------------------------------------------------

## ==============Array properties=================

#------------------------------------------------

arr = np.array([[1,2,3],[4,5,6]])

# print("shaape",arr.shape)
# print("dtamention",arr.ndim)
# print("size",arr.size)
# print("data  type",arr.dtype)
# print("array",arr)

#-----------------------------------------------

##====== Array reshaping ======================

#---------------------------------------------

arr = np.arange(12)
print(" Orignal array",arr)

reshapped = arr.reshape((3,4))
print(" reshapped  array",reshapped)

flattend = reshapped.flatten()
print(" flattened array",flattend)

#return viwe,instead of copy

raveld =reshapped.ravel()
print(" Raveld array",raveld)

#Transpose

transpose = reshapped.T
print("transpose array",transpose)

#-----------------------------------------

