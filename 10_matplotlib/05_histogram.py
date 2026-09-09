###=========Histogram  Chart =====================

import matplotlib.pyplot as plt
import random
#  data-----------------

data = [random.randint(1,10) for _ in range(100)]

plt.hist(data,bins=4)
plt.title('histogram chart')
plt.show()