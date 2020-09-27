def cube():
    for i in range(50):
        yield i ** 3


for i in cube():
    print(i)

# *******************************#

generator = (i ** 5 for i in range(5))
print(generator)

for i in generator:
    print(i)