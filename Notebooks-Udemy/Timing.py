__author__ = 'alakus'

from timeit import timeit

# for loop
print timeit('"-".join(str(n) for n in range(100))', number=10000)

# List comprehension
print timeit('"-".join([str(n) for n in range(100)])', number=10000)

# Map()
print timeit('"-".join(map(str, range(100)))', number=10000)
