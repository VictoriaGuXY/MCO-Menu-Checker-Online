from array import array
from random import  random
from collections import deque

"""
output
"""

# This file introduces the use of array() and deque() in python.

#-------------------------------------------------------------------------------
# first parameter represents value type, e.g. float, char, etc.
# second parameter represents data
# 'd' stands for double

data = array('d', (random() for i in range(10**7)))

# output last element
print(data[-1])

"""
0.9218269523324655
"""

#-------------------------------------------------------------------------------
# array provides many useful methods to deal with the data, like pop, insert
# it also provides tofile and frombytes to write in and read in file

with open('data.bin', 'wb') as fp:
    data.tofile(fp)
    
#-------------------------------------------------------------------------------
# use of deque
# first parameter is data
# second parameter is largest size of deque, default is inifinite size
data = deque(range(10), maxlen = 3)
print(data)

"""
deque([7, 8, 9], maxlen=3)
"""

data.append(3)
# if the 4th number is added, 7 is removed from deque
print(data)
data.pop()
print(data)

"""
deque([8, 9, 3], maxlen=3)
deque([8, 9], maxlen=3)
"""
