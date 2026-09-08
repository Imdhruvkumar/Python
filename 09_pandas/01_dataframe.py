## ========== import pandas ===============

import pandas as pd

#-------------create data frame -------------

df = pd.DataFrame([1,2,3,4,5],columns=["col_name"])
# print(df)
# print(type(df))


data = {
    'name':['dhruv','kuar','amar','kamar'],
    'class':['first','second','third','forth'],
    'age' :[23,45,67,89]


}

df  = pd.DataFrame(data)

# print(df)
# print(type(df))

##======= Basic data frame understanding =================

#-------top rows and bdefault row(5)-----


# head() how many rows want to print

# print(df.head(2))
# print(df.head())
# print(df.head(6))

# print("rows fron ends\n",df.tail(2))

# print(df.shape)
# print(df.columns)
df.rename(columns={'age':'m_age'})
# print(r_data)
# print(df)


# df.info()

# print(df.describe())




