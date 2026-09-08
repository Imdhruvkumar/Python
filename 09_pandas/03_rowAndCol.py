## ====== row and columns selections =============

import pandas as pd

data = {
    'name':['dhruv','kuar','amar','kamar'],
    'class':['first','second','third','forth'],
    'age' :[23,45,67,89]


}

df  = pd.DataFrame(data)

# ------- select  specific columns --------------

# print(df[['name','age']])

#  selecting row  base name with any condition

row = df.loc[(df.name=='dhruv') & (df.age >= 1) ]

# print(row)

## select particular index 
# print(df.iloc[2])

## multiple rows
# print(df.iloc[0:2])

