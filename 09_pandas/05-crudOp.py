#====== row and columns poeration add,update,delete========
import pandas as pd

data = {
    'name':['dhruv','kuar','amar','kamar'],
    'class':['first','second','third','forth'],
    'age' :[23,45,67,89]

}

df  = pd.DataFrame(data)

# print(df)

## ====== add new columns ================

df['team'] = ['ceo','hr','md','dm']

# print(df)

df['ad_age'] = df['age'] * 2

# print(df)

## ======== Add new row ====================

df.loc[len(df)] = ['abs','xxx',11,'df',200]

# print(df)

## ========== value update ===================

df.loc[0,'name'] = "kala"

# print(df)


##======== value delete row wise =======================

df.drop(df[df.name == "abs"].index,inplace=True)
# print(df)

df.drop("ad_age",axis=1,inplace=True)
# print(df)


## ======= Sorting ======================


df.sort_values('age',inplace=True)

df.sort_values('age',ascending=False,inplace=True)# desending order

print(df)