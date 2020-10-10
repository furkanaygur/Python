import pandas as pd

numbers = [50, 60, 70, 80, 90]
pandas_series = pd.Series(numbers)
print(pandas_series)

letters = ['f', 'u', 'r', 'k', 'a', 'n', 22]
pandas_series = pd.Series(letters)
print(pandas_series)

scalar = 5
pandas_series = pd.Series(scalar)
print(pandas_series)

pandas_series = pd.Series(5, [0, 1, 2, 3, 4])
print(pandas_series)

pandas_series = pd.Series(5, ['a', 'b', 'c', 'd'])
print(pandas_series)

dict = {'a': 10, 'b': 20, 'c': 30}
pandas_series = pd.Series(dict)
print(pandas_series)

# With numpy
import numpy as np

random_numbers = np.random.randint(10, 100, 5)
pandas_series = pd.Series(random_numbers)
print(pandas_series)

numbers = np.array([50, 60, 70, 80, 90])
pandas_series = pd.Series(numbers)
print(pandas_series)

# *********************************************
# *********************************************

pandas_series = pd.Series([50, 60, 70, 80, 90])
result = pandas_series[0]
print(result)

pandas_series = pd.Series([50, 60, 70, 80, 90], ['a', 'b', 'c', 'd', 'e'])
result = pandas_series['c']
print(result)

result = pandas_series[['c', 'e']]
print(result)

# Example
opel2018 = pd.Series([20, 30, 10, 50], ["astra", "corsa", "mokka", "insignia"])
opel2019 = pd.Series([40, 15, 50, 20], ["astra", "corsa", "Grandland", "insignia"])

total = opel2018 + opel2019
print(total["astra"])

