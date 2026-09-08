##======= handling mising value==================

import pandas as pd
import numpy as np

data = {
    'name':['dhruv','kuar','amar','kamar'],
    'class':['first','second','third','forth'],
    'age' :[23,45,67,89]

}

df  = pd.DataFrame(data)
# print(df)

df.loc[df.name =='dhruv','age'] = np.nan
# print(df)

# df.isnull()
# print(df.isnull())

# print(df.isnull().sum())

print(df.fillna(0))
