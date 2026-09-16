# import matplotlib.pyplot as plt
# plt.plot([1,2,3],[4,5,6])
# plt.show()
import matplotlib.pyplot as plt
import numpy as np

plt.plot(np.random.rand(100), linewidth=1)

plt.title("Too Much Data Can Be Confusing!")
plt.grid(True)
plt.tight_layout()
plt.show()