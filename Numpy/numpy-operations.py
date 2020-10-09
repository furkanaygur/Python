import numpy as np

numbers1 = np.random.randint(10, 100, 6)
numbers2 = np.random.randint(10, 100, 6)

print("Numbers1: ", numbers1, "\n Numbers2: ", numbers2)
# ***********************************************
result = numbers1 + numbers2
print(result)
# ***********************************************
result = numbers1 + 10
print(result)
# ***********************************************
result = numbers1 * numbers2
print(result)
# ***********************************************
# result = np.sin(numbers1)
# result = np.cos(numbers1)
# result = np.sqrt(numbers1)
result = np.log(numbers1)
print(result)
# ***********************************************
multi_numbers1 = numbers1.reshape(2, 3)
multi_numbers2 = numbers2.reshape(2, 3)
print(multi_numbers1, "\n", multi_numbers2)
# ***********************************************
result = np.vstack((multi_numbers1, multi_numbers2))
print("Veritcal: \n", result)
# ***********************************************
result = np.hstack((multi_numbers1, multi_numbers2))
print("Horizontal: \n", result)
# ***********************************************
result = numbers1 >= 50
print(result)
print(numbers1[result])
# ***********************************************

