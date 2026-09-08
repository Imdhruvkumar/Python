##====== aggregation and group by ===========

import pandas as pd
import numpy as np

data = {
    'name':['dhruv','kuar','amar','kamar'],
    'class':['first','second','third','forth'],
    'age' :[23,45,67,89]

}

df  = pd.DataFrame(data)

df['team'] = ['ceo','ms','md','hr']

# print(df)

# print(df['team'].value_counts())
df['DOJ'] = ['2024-03-01','2024-02-04','2024-08-07','2024-08-01',]

df['DOJ'] = pd.to_datetime(df['DOJ'])
df['month'] = (df['DOJ'].dt.month)

# print(df)


# print(df['team'].value_counts())

# print(df[df['month']==8].value_counts())

# print(df.groupby('month')['age'].sum())
# print(df.groupby('month')['age'].mean())