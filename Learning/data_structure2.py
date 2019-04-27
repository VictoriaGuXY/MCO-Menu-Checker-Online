import heapq

"""
output
"""

# This file introduces the use of heapq and dictionary and how to find largest 
# and smallest elements in these two data structures.

#-------------------------------------------------------------------------------
# use of heapq
# We can do 'sorting' in heapq
# so we are able to find the largest or smallest n elements in it
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# find largest 3 numbers
print(heapq.nlargest(3, nums))

"""
[42, 37, 23]
"""

# find smallest 3 numbers
print(heapq.nsmallest(3, nums))

"""
[-4, 1, 2]
"""

# Note:
# nlargest can find the largest n elements in heapq
# In opposite, nsmallest can find the smallest n elements in heapq

#-------------------------------------------------------------------------------
# if the data structure is dictionary

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# we want to search dictionary in order of prices
# key can find prices in dictionary
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

print(cheap)
print(expensive)

"""
[{'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75}]
[{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}, {'name': 'IBM', 'shares': 100, 'price': 91.1}]
"""
