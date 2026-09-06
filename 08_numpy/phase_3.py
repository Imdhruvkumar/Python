##===========Advance operation  with business example========

#---Data structure:[restaurent id,2020,2021,2022,2023,2024]

import numpy as np
import matplotlib.pyplot as plt
data = np.array([
    [1, 40000, 50000, 60000, 70000, 80000],# "Biryani"
    [2, 30000, 40000, 50000, 60000, 70000],# "Pizza"
    [3, 20000, 30000, 40000, 50000, 60000],# "Dosa"
    [4, 25000, 35000, 45000, 55000, 65000],# "Burger"
    [5, 35000, 45000, 55000, 65000, 75000] # "Paneer Tikka"
])

print("==== detail analysis ====")
# print("\n sales data shape",data.shape)
# print("\n sales data size",data.size)
# print("\n first three salse data \n",data[:3])
# print("\n specific single column  data \n",data[:,3])
# print("\n lower than thrid column data \n",data[:,:3])
# print("\n greater than thrid column data \n",data[:,3:])


##========== total sales per year =====================

# print("adding data column wise\n",np.sum(data,axis=0))
# print("adding data row wise\n",np.sum(data,axis=1))

# print("adding data except first col \n",np.sum(data[:,1:],axis=0))
# print("adding data except first col \n",np.sum(data[:,1:],axis=1))


yearly_total = np.sum(data[:,1:],axis=0)

# print("yearlt total ",np.sum(yearly_total))

#=========minimum sales per restaurent ================

