import matplotlib.pyplot as plt
import numpy as np
from pnoise import PerlinNoiseFactory

pnf = PerlinNoiseFactory(2, octaves=1)

frameSize = 200
X, Y = np.meshgrid(np.arange(0, frameSize, 1.0), np.arange(0, frameSize, 1.0))
current = np.zeros((frameSize, frameSize))

for i in range(frameSize):
    for j in range(frameSize):
        current[i,j] = pnf(i/frameSize,j/frameSize)

dy, dx = np.gradient(current)

fig, axs = plt.subplots(ncols=3, nrows=2)
gs = axs[0, 1].get_gridspec()

for ax in axs[0:, -1]:
    ax.remove()
for ax in axs[0:, -2]:
    ax.remove()
axbig = fig.add_subplot(gs[:, 1:])

axs[0, 0].set_title("Perlin Noise")
axs[0, 0].imshow(current[::-1, :])
axs[0, 0].set_aspect("equal", 'box')

axbig.set_title("Contour Plot")
axs[1, 0].contour(X, Y, current, colors=["black"])
axs[1, 0].contourf(X, Y, current)
axs[1, 0].set_aspect("equal", 'box')

axbig.set_title("Stream Plot")
axbig.set_aspect("equal", 'box')
cs = axbig.contourf(X, Y, current)
axbig.streamplot(np.arange(0, frameSize, 1), np.arange(0, frameSize, 1), dx, dy, color='black', density=1)
fig.colorbar(cs)

plt.tight_layout()
plt.show()