cars = ["Bmw", "Mercedes", "GTR", "Lambo"]
result = len(cars)
print(result)
cars[-1] = 'Lamborghini'
print(cars)
result = 'GTR' in cars
print(result)
result = cars[:2]
print(result)
cars[-2:] = ['Lamborghini', 'GTR']
result = cars
print(result)
result = cars + ['Audi', 'Renault']
print(result)
del result[-2:]
print(result)
result = cars[::-1]
print(result)
# -------------------------------------- #
numbers = [1, 2, 3, 4, 5, 12, 12, 56, 2, -1]
letters = ['f', 'u', 'r', 'k', 'a', 'n']
value = min(numbers)
print("\n", value)
value = max(numbers)
print(value)
value = min(letters)
print(value)
value = max(letters)
print(value)
numbers.append(57)
print(numbers)
numbers.insert(2, 75)
print(numbers)
numbers.pop()  # delete last index value
print(numbers)
numbers.remove(12)
print(numbers)
numbers.sort()
print(numbers)
letters.sort()
print(letters)
numbers.reverse()
print(numbers)
letters.reverse()
print(letters)
print(len(letters))
letters.clear()
print(letters)
