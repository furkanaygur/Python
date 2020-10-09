import numpy as np

numbers = np.array([0, 5, 10, 15, 20, 25, 50, 75])

result = numbers[5]
print(result)
# ***********************************************
result = numbers[-1]
print(result)
# ***********************************************
result = numbers[3:]
print(result)
# ***********************************************
# ***********************************************
numbers2 = np.array([[0, 5, 10], [15, 20, 25], [50, 75, 85]])
print(numbers2)

result = numbers2[0]
print(result)
# ***********************************************
result = numbers2[0, 2]
print(result)
# ***********************************************
result = numbers2[:, 0]
print(result)
# ***********************************************
result = numbers2[:, 0:2]
print(result)
# ***********************************************
result = numbers2[-1:]
print(result)
# ***********************************************
result = numbers2[:2, :2]
print(result)
# ***********************************************
array = np.arange(0, 10)
# array2 = array  # reference
array2 = array.copy()
# ***********************************************