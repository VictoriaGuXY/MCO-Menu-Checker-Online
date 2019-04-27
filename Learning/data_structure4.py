"""
output
"""

# This file introduces the methods to find data in list with a constraint.
# Methods includes use list comprehension and generator.
# To get a part of list, we can use slice().


# find all data from list that are <10 without using iterations
# using list comprehension
datas = [3, 4, 2, 8, 12, 5, 7]
print([data for data in datas if data<10])

"""
[3, 4, 2, 8, 5, 7]
"""

# if we have many data, it's better to use a generator.
# Generatoe is initialized using bracket ()
r = (data for data in datas if data<10)

# nothing is printed if we write the following code
print(r)

# but now, it is printing
# enumerate returns index and element at the same time
for i, j in enumerate(r):
    print(i, j)
    
"""
<generator object <genexpr> at 0x000001EA20F3F678>
0 3
1 4
2 2
3 8
4 5
5 7
"""

# Note: generator can only be used once in iterateration
# If we print(i, j) once again, nothing is printed.

#-------------------------------------------------------------------------------
# If we want a specific data or specific part of data from the list

a = [2, 3, 'a', 6, 4]
print(a[3:4])

"""
[6]
"""

b = 'hahahah'
print(b[::2])
print(b[::-1])

"""
hhhh
hahahah
"""

c = (2, 2, 3, 4, 5)
print(c[:3])

"""
(2, 2, 3)
"""

# The above method needs us to remember the starting index and ending index.
# slice is much easier

items = [1, 2, 3, 4, 5, 6, 7]

# we say this slice is from 2 to 4, has size 2
a = slice(2, 4)
print(a)
print(items[a])

"""
slice(2, 4, None)
"""

# We can also apply this to other structures.
itemss = [1, 2, 4, 6, 5, 6, 7]
print(itemss[a])

"""
[3, 4]
[4, 6]
"""
