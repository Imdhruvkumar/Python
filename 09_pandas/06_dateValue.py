##=========== working with date value ===========

import pandas as pd

data = {
    'name':['dhruv','kuar','amar','kamar'],
    'class':['first','second','third','forth'],
    'age' :[23,45,67,89]


}

df  = pd.DataFrame(data)

df['DOJ'] = ['2024-03-01','2024-02-04','2024-08-07','2024-08-01',]

# print(df)
# print(df['DOJ'].dtype)


df['DOJ'] = pd.to_datetime(df['DOJ'])
# print(df['DOJ'].dtype)

df1= df
# print(df1)

df1['DOJ1'] = ['12-03-2034','12-03-2034','12-03-2034','12-03-2034',]


# print(df1)
df1['DOJ1'] = pd.to_datetime(df1['DOJ1'])

# print(df1['DOJ1'].dtype)


df=df.drop('DOJ1',axis=1)
# print(df)

## --------  find years aur months ---------

# print(df['DOJ'].dt.month)
# print(df['DOJ'].dt.year)
# print(df['DOJ'].dt.day)
# print(df['DOJ'].dt.day_name())

