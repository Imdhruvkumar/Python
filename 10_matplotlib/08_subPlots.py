# =========== sub plots =================
#used to multiple charts


# data =================
import matplotlib.pyplot as plt
# bar chart
cato= ['a','b','c','d','e']
lables = [10,20,30,40,50]

#scatter chart
y = [10,20,30,40,50]
y1= [17,27,37,47,56]

plt.figure(figsize=(10,6))
plt.subplot(1,2,1)# row,columns,position

plt.bar(cato,lables)
plt.title('weekly chart')
plt.xlabel('weeks')
plt.ylabel('sales')

plt.subplot(1,2,2)
plt.scatter(y,y1)
plt.title('user example')
plt.xlabel('weeks')
plt.ylabel('sales')


plt.show()
