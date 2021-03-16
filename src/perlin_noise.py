import matplotlib.pyplot as plt
import numpy as np
from pnoise import PerlinNoiseFactory

pnf = PerlinNoiseFactory(2, octaves=2)

frameSize = 200
X, Y = np.meshgrid(np.arange(0, frameSize, 1.0), np.arange(0, frameSize, 1.0))
current = np.zeros((frameSize, frameSize))

for i in range(frameSize):
    for j in range(frameSize):
        current[i,j] = pnf(i/frameSize,j/frameSize)

dy, dx = np.gradient(current)

fig, axs = plt.subplots(ncols=2, nrows=2)

axs[0, 0].set_title("Perlin Noise")
axs[0, 0].imshow(current[::-1, :])
axs[0, 0].set_aspect("equal", 'box')

axs[1, 0].set_title("Contour Plot")
axs[1, 0].contour(X, Y, current, colors=["black"])
axs[1, 0].contourf(X, Y, current)
axs[1, 0].set_aspect("equal", 'box')

axs[0, 1].set_title("Stream Plot")
axs[0, 1].set_aspect("equal", 'box')
cs = axs[0, 1].contourf(X, Y, current)
axs[0, 1].streamplot(np.arange(0, frameSize, 1), np.arange(0, frameSize, 1), dx, dy, color='black', density=1)
# fig.colorbar(cs)

axs[1, 1].set_title("Quiver Plot")
axs[1, 1].set_aspect("equal", 'box')
axs[1, 1].quiver(X[::4, ::4], Y[::4, ::4], dx[::4, ::4], dy[::4, ::4])


# plt.tight_layout()
fig.set_size_inches(7, 7)
plt.show()
