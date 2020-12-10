import math

import matplotlib.pyplot as plt
import numpy as np

x, y = np.mgrid[-2:2:200j, -2:2:200j]
z = (1 / 2 * math.pi * 3 ** 2) * np.exp(-(x ** 2 + y ** 2) / 2 * 3 ** 2)
ax = plt.subplot(111, projection='3d')
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='rainbow', alpha=0.9)  # 绘面

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
