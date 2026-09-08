## concatenate and merge +======================
import pandas as pd
df1= pd.DataFrame({
    'id':[1,2,3],
    'name':['a','b','c']
})

# print(df1)

df2= pd.DataFrame({
    'id':[1,2,2,4],
    'score':[46,75,86,88]
})

# print(df2)
## ------------ concatenate two data frame--------------

df3 = pd.concat([df1,df2],axis=1)
# print(df3)

##======== merge = join ===============


# df4 = pd.merge(df1,df2,how='inner',on='id')
# df4 = pd.merge(df1,df2,how='outer',on='id')

df4 = pd.merge(df1,df2,how='inner',on='id')

print(df4)