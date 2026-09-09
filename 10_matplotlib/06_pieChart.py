## ============= pie chart ===========

# data =================
import matplotlib.pyplot as plt
x= ['a','b','c','d','e']
y = [10,20,30,40,50]
plt.pie(y, labels=x, autopct='%1.1f%%')
plt.title('kuch bhi')
plt.show()