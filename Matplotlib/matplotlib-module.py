import matplotlib.pyplot as plt
import numpy as np


# ***************************************

# x = [1,2,3,4]
# y = [1,4,9,16]

# plt.plot(x, y ,"o--r", linewidth="2")
# plt.axis([0,6,0,20])
# plt.title("Graphic Title")
# plt.xlabel("X Label")
# plt.ylabel("Y Label")


# plt.show()

# ***************************************

# x = np.linspace(0,2,100)
# plt.plot(x, x, label='linear' , color="red")
# plt.plot(x, x**2, label='quadratic', color="blue")
# plt.plot(x, x**3, label='cubic', color="green")

# plt.xlabel("X Label")
# plt.ylabel("Y Label")

# plt.legend()

# plt.title("Simple Plot")

# plt.show()

# ***************************************

# x = np.linspace(0,2,100)

# fig, axs = plt.subplots(3)
# axs[0].plot(x, x, color="red")
# axs[0].set_title("linear")

# axs[1].plot(x, x**2, color="green")
# axs[1].set_title("quadratic")

# axs[2].plot(x, x**3, color="yellow")
# axs[2].set_title("cubic")

# plt.tight_layout()

# plt.show()


# ***************************************

# x = np.linspace(0,2,100)
# fix, axs = plt.subplots(2,2)
# fig.suptitle("Graphic Title")

# axs[0,0].plot(x, x, color="red")
# axs[0,1].plot(x, x, color="green")
# axs[1,0].plot(x, x, color="blue")
# axs[1,1].plot(x, x, color="orange")

# plt.show()

# ***************************************

import pandas as pd

df = pd.read_csv("nba.csv")

df = df.drop(["Number"], axis=1).groupby("Team").mean()

df.head().plot(subplots=True)
plt.legend()
plt.show()