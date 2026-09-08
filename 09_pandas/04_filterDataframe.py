## ========= Filter dataframe =======================

import pandas as pd

data = {
    'name':['dhruv','kuar','amar','kamar'],
    'class':['first','second','third','forth'],
    'age' :[23,45,67,89]

}

df  = pd.DataFrame(data)

print(df[df['age'] >50])

# print(df[(df['age'] >50) & (df['name']=='amar')])

print(df.where((df['age'] >50),other='not ele'))