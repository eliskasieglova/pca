from matplotlib import pyplot as plt
import numpy as np

"""x = [2, -5, -1000, 1, 89, 1500, 13, 23, -49, 120]
y = [1, 487, -82, -1, 139, 12, -4, -68, 2, 10]"""


x = [1, 2, 3, 4, 5, 7, 7, 8, 9, 10]
y = [2, 4, 6, 7, 10, 11, 13, 15, 17, 20]


c = np.cov(np.asarray([x, y]))

D, v = np.linalg.eig(c)

print(D)
print(v)

print(D[1]/(D[1]+D[0]))

plt.plot(x, y, 'bo')
#plt.show()






