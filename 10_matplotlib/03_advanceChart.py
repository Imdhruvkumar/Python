## ========= multipe line chart  ====================

import matplotlib.pyplot as plt

#  data-----------------

x= [1,2,3,4,5]

y = [10,20,36,40,50]
y1= [15,25,36,45,58]
plt.figure(figsize=(4,4))
plt.plot(x,y,label='Sales 2024') #ploting y data
plt.plot(x,y1,label='Sales 2025')#ploting y1 data
plt.title('kuch bhi title hai')
plt.xlabel('months')
plt.ylabel('sales')
plt.legend()
plt.grid(True)
plt.show()# want to display