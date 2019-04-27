# This file introduces unpack
# Unpack: assign a list or string to multiple variables at the same time
# can use unpack if can use iteration 

a, b, c = [1, 2, 4]
print(a)

a, b = 'it'
print(a)

"""
1
i
"""

#-------------------------------------------------------------------------------
# If we have so many data, use * to represent the rest of data and use _ to 
# represent data I don't need.

data = [1, 2, 3, 4, 5, 6]

# This is ok
a, b, *r = data
print(r)

# This is also ok
*a, b, c, d = data
print(a)

"""
[3, 4, 5, 6]
[1, 2, 3]
"""
