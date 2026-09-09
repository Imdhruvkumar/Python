## ========= customize first chart  ====================

import matplotlib.pyplot as plt

#  data-----------------

x= [1,2,3,4,5]

y = [10,20,36,40,50]
plt.figure(figsize=(4,4))
plt.plot(x,y,color='red',marker='o',linestyle='dashed',linewidth=2,markersize=12)
plt.title('kuch bhi title hai')
plt.xlabel('months')
plt.ylabel('prices')
plt.grid(True)
plt.show()# want to display