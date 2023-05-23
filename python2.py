import math
from math import sqrt, floor, ceil, pow

'''
import time
result = 0
t_start = time.time()
for i in range(1000001):
    result += i**2
print(result)
t_end = time.time()
print(t_end - t_start)

import os
# operating system

# Pathing
# 'text.txt'
# 'nameoffile'

# check a file exists
# os.path.exists('nameoffile')

# check if a file existed
# os.path.isdir('file')
# os.path.exists('file')

# list files in folder
# print(os.listdir('file'))
'''

# raise
'''
year = int(input())
# assert year < 2023
if year < 1900 or year > 2023:
    raise ValueError('Invalid year')
print(2023-year)'''

# function
# 1 in 1 out
'''def square(x):
    result = x**2
    return result

n = int(input())
squareofn = square(n) # print(square(n))
print(squareofn)'''

# many in 1 out
def power(x, y):
    result = x**y
    return result
print(power(3,3))