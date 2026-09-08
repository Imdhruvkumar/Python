## ======== save and load data from  csv ================
import pandas as pd

data = {
    'name':['dhruv','kuar','amar','kamar'],
    'class':['first','second','third','forth'],
    'age' :[23,45,67,89]


}

df  = pd.DataFrame(data)
# print(df)

## ========= save data to csv ==============

# df.to_csv('test_csv.csv',index=False)

#============data load from csv==================
load = pd.read_csv('test_csv.csv')
# print(load)