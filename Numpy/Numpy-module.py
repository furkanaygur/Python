import numpy as np

# ************************************************
np_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(type(np_array))
# ***********************************************
np_multi = np_array.reshape(3, 3)
print(np_multi, "\n Dimension: ", np_multi.ndim, "\n Shape: ", np_multi.shape)
# ***********************************************
result = np.arange(1, 20, 2)
print(result)
# ***********************************************
result = np.zeros(10)
print(result)
# ***********************************************
result = np.ones(10)
print(result)
# ***********************************************
result = np.linspace(0, 100, 5)
print(result)
# ***********************************************
result = np.random.randint(0, 10)
print(result)
# ***********************************************
result = np.random.randint(1, 10, 3)
print(result)
# ***********************************************
result = np.random.randn(5)
print(result)
# ***********************************************
result = np.random.randn(5)
print(result)
# ***********************************************
np_array = np.arange(1, 51)
np_multi = np_array.reshape(5, 10)
print(np_multi)
print("sum of rows:", np_multi.sum(axis=1))
print("sum of column:", np_multi.sum(axis=0))
# ***********************************************
rnd_numbers = np.random.randint(1, 100, 10)
print(rnd_numbers)
print("Max:", rnd_numbers.max())
print("Min", rnd_numbers.min())
print("Avg:", rnd_numbers.mean())
print("Max in the index:", rnd_numbers.argmax())
print("Min in the index:", rnd_numbers.argmin())
# ***********************************************
