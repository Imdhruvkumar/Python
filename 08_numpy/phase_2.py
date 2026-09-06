# ======= numpy array operation ==========

#---------------------------------------------

import numpy as np

arr = np.array([1,2,3,4,5,6])
# print("Basic Slicing",arr[0])
# print("Basic Slicing",arr[2:3])
# print("Basic Slicing",arr[-1])
# print("Basic Slicing",arr[4])
# print("Basic Slicing",arr[-5])

arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [6,7,8]])

# print("spesic element",arr_2d[1,1]) #spesic element 5
# print("entire row",arr_2d[1]) 
# print("entire column",arr_2d[:,1]) 

#--------------------------------------------

#===== sorting in numpy==============

#-------------------------------------------

unsorted = np.array([3,6,8,5,4,12,1])

# print("sorted",np.sort(unsorted))

arr_2d_unsorted = np.array([[2,1],
                            [3,2],
                            [1,3]])

# print("sorting column in 2d",np.sort(arr_2d_unsorted, axis=0))


# print("sorting row in 2d",np.sort(arr_2d_unsorted, axis=1))


#==========Filter============================

#---------------------------------------------

num_arr = np.array([1,2,3,4,5,6,7,8])

even_num = num_arr[num_arr % 2 == 0]
# print("even numbers",even_num)


#------filter with mask ------------------

mask = num_arr>5
# print("number greater than 5 ",num_arr[mask])

##======= Fancy Indexing and np.where()==============

indices =[0,2,4]
# print(num_arr[indices])

where_result = np.where(num_arr>5)
# print("np where",num_arr[where_result])

numbers = np.array([1,2,3,4,5,6,7,8,9,10])
condition_array = np.where(numbers >5,"true","false")

# print("condition array",condition_array)


#=== Adding and removing ====================

array1 = np.array([3,4,5,6,7])
array2 = np.array([1,2,5,6,7,8])
combind = np.concatenate((array1,array2))

# print(combind)

 
#========= array compeletibilty =============

a = np.array([1,2,3])
b = np.array([5,4,6])
c = np.array([6,7,8])

# print("compatibility shape",a.shape == b.shape)

orignal = np.array([[1,2],[4,5]])

new_row = np.array([2,6])

with_new_row = np.vstack((orignal,new_row))
# print(orignal)
# print(with_new_row)

new_column = np.array([[7],[6]])

with_column = np.hstack((orignal,new_column))
# print(with_column)


#=======Delete===================

arr= np.array([1,2,3,4,5])

deleted = np.delete(arr,2)
print(deleted)