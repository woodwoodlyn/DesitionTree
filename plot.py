
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
data = np.array([[1,1,1,0,0],[1,1,1,0,0],[0,0,0,2,2],[0,0,0,2,2]])
test0 = [[i,j,data[i,j]] for i in range(4) for j in range(5)]
test = np.array(test0)


xs = np.arange(20)
ys = np.random.rand(20)
# ax.bar(xs, ys, zs=30,zdir='y',alpha=0.8)

for i in range(data.shape[0]):

    xs = [i]*(data.shape[1])
    ys = range(data.shape[1])
    ax.bar(xs, ys, data[i,:], zdir='y', alpha=0.8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

fig = plt.figure()
ax = fig.gca(projection='3d')
test0 = [[i,j,data[i,j]] for i in range(4) for j in range(5)]
test = np.array(test0)
surf = ax.plot_surface(test[:,0], test[:,1], test[:,2], cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(0, 5)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(test[:,0], test[:,1], test[:,2])
plt.show()