## =========matplotlib with pandas with real data==========
import matplotlib.pyplot as plt

# create dataframe
import pandas as pd

data = {
    'month':['mon','tue','wed','thu'],
    'salse':[2500,52582,3145,26547],
    }

df = pd.DataFrame(data)


plt.bar(df['month'],df['salse'])

plt.title('weekly chart')
plt.xlabel('month')
plt.ylabel('sales')
# plt.savefig('subplot_chart.png')
plt.show()