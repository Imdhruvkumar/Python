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

#------------------------------------------------

min_sales = np.min(data[:,1:],axis=0)

# print("column wise min data",min_sales)

min_sales = np.min(data[:,1:],axis=1)

# print("row wise min data",min_sales)

#=========maximum sales per restaurent ================

max_sales = np.max(data[:,1:],axis=0)

# print("max sale cloumn ",max_sales)


max_sales = np.max(data[:,1:],axis=1)

# print("max sale row wise",max_sales)

##===============average salse per restaurent==============

avg_sales = np.average(data[:,1:],axis=0)

# print("average column wise",avg_sales)

avg_sales = np.average(data[:,1:],axis=1)

# print("average row wise",avg_sales)

#=============cumletive ====================
#-----------adding row wise year per year-----

cumsum = np.cumsum(data[:,1:],axis=1)
# print(cumsum)
# print(np.mean(cumsum,axis=0))
#============= Using matplotlib ================

# plt.figure(figsize=(8,5))
# plt.plot(np.mean(cumsum,axis=0))
# plt.title("Average cumlative sales accoros all restaurent")
# plt.xlabel("years")
# plt.ylabel("sales")
# plt.grid(True)
# plt.show()

#============vecter========================

vecter1 = np.array([1,2,3,4,5])

vecter2 = np.array([6,7,8,9,0])

# print("vecter addition",vecter1+vecter2)

# print("multilication of vecter",vecter1*vecter2)

# print("dot product",np.dot(vecter2,vecter1))


rest_types = np.array(["green","maxican","orfin"])
vecterized_upper = np.vectorize(str.upper)
# print("vectorised upper",vecterized_upper(rest_types))

monthly_avg = data[:,1:] / 12

print(monthly_avg)