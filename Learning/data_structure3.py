from collections import namedtuple

"""
output
"""

# This file introduces the namedtuple
# Sometimes we need a class to represent one thing, but we do not need to define
# a class and write lots of codes.
# namedtuple helps us to quickly create a class.

# The first parameter is the name of class
# The second parameter is data in class. It can be a string, or a list of string.
Student = namedtuple("Student", ['name', 'age', 'id'])
Studen = namedtuple("Studen", "name age id")
s1 = Studen('zhuzhezhe', '23', '001')
s2 = Student('zhuzhezhe', '23', '001')

print(s1)
print(s2)

"""
Studen(name='zhuzhezhe', age='23', id='001')
Student(name='zhuzhezhe', age='23', id='001')
"""
