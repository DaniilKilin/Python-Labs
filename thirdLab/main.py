from pyDatalog import pyDatalog
from random import randrange
import numpy

n = 1000000
nn = 100

pyDatalog.create_terms('sum_of_range, N, Sum_of_range')

sum_of_range[N] = (0 + N) * n/2
print(sum_of_range[n] == Sum_of_range)
print()

pyDatalog.create_terms(' medium, Medium')
medium[N] = sum_of_range[N] / N
print(medium[n] == Medium)
print()

pyDatalog.create_terms('median, Median')

median = nn/2
print(median == Median)
print()

pyDatalog.create_terms('Factorial, Prod')
Factorial[N] = N * Factorial[N - 1]
Factorial[1] = 1
print(Prod == Factorial[nn])
