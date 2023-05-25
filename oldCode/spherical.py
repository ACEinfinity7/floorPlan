import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


# roe = np.linspace(1, 2, 100)
# theta = np.linspace(0, 2*np.pi, 100)
# phi = np.linspace(np.pi/2, np.pi, 100)
# theta, phi = np.mgrid[0:2*np.pi:10j, np.pi/2.01:np.pi:10j]
# roe, theta, phi = np.meshgrid(np.arange(1, 2, 0.1),
#   np.arange(0, 2.0*np.pi, 0.01),
#   np.arange(np.pi/2, np.pi, 0.1))
# print(theta)

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# roe0, roe1 = 1, 2
# theta0, theta1 = 0, np.pi * 2
# phi0, phi1 = np.pi / 2, np.pi
# roe = np.linspace(roe0, roe1, 10)
# theta = np.linspace(theta0, theta1, 100)
# phi = np.linspace(phi0, phi1, 10)

# x, y, z = [], [], []

# for r in roe:
#     for t in theta:
#         for p in phi:
#             x.append(r * np.sin(p) * np.cos(t))
#             y.append(r * np.sin(p) * np.sin(t))
#             z.append(r * np.cos(p))
# # print(z)
# ax.set_xlim3d(left=-5, right=5)
# ax.set_ylim3d(bottom=-5, top=5)
# ax.set_zlim3d(bottom=-5, top=5)

# ax.scatter(x, y, z, )
# plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

theta, phi = np.linspace(0, 2 * np.pi, 40), np.linspace(0, np.pi/3, 40)
THETA, PHI = np.meshgrid(theta, phi)
# r = np.linspace(1, 2, 10)
r0, r1 = 0, 1

r = [x/10 for x in range(r0*10, r1*10, 1)]
for R in r:
    X = R * np.sin(PHI) * np.cos(THETA)
    Y = R * np.sin(PHI) * np.sin(THETA)
    Z = R * np.cos(PHI)
    ax.plot_surface(
        X, Y, Z, cmap=plt.get_cmap('RdGy'),
        linewidth=10, antialiased=True, alpha=(0.5))
# plot =

plt.show()
