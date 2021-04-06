import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 4, 1)

y1 = x
y2 = x**2
y3 = x**3

fig, ax = plt.subplots()
#ax.plot (x, y1, 'g.',label="X**1")
#ax.plot(x, y2,  'r.', label="X**2")
#ax.plot(x, y3, 'b.', label="X**3")

ax.plot(x, y1, linewidth=2.0, linestyle='--', color='g', label="X**1", alpha=1, marker='o')
ax.plot(x, y2, linewidth=2.0, linestyle=':', color='r', label="X**2", alpha=1, marker='o')
ax.plot(x, y3, linewidth=2.0, linestyle='-', color='b', label="X**3", alpha=1, marker='o')

ax.grid(True)
ax.legend()

plt.title("HomeWork Week 8")
plt.xlabel("Axe X")
plt.ylabel("Axe Y")

plt.ioff()
plt.show()


