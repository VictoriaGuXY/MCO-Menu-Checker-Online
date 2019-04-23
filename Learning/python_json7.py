import json

"""
output
"""

# This file contains notes to more use of JSON in Python and the convertion
# between them.

# ------------------------------------------------------------------------------
# If we set variable 'sort_keys' as True, then the resulting JSON object is
# sorted based on keys.
# The original value of 'sort_keys' is set as False.

dic = {'b':'I', 'a':123, 'c':'100'}
j1 = json.dumps(dic, sort_keys = True)
print (j1)

""" 
{"a": 123, "b": "I", "c": "100"}
"""

# ------------------------------------------------------------------------------
# We can use 'indent' to set the indentation of resulting JSON object.

dic = {'b':'I', 'a':123, 'c':'100'}
j2 = json.dumps(dic, sort_keys = True, indent = 4)
print (j2)

"""
{
    "a": 123,
    "b": "I",
    "c": "100"
}
"""

# ------------------------------------------------------------------------------
# We can use 'separators' to set separation character of resulting JSON object.

dic = {'b':'I', 'a':123, 'c':'100'}
j3 = json.dumps(dic, sort_keys = True, separators = ('$','@'))
print (j3)

"""
{"a"@123$"b"@"I"$"c"@"100"}
"""

# ------------------------------------------------------------------------------
# List can be converted to JSON.

list1 = [1, 'big', [1, 'a', {'p':'+'}], (['t',2],{'1':'o'}), {'c':0,'d':1}]
j4 = json.dumps(list1)
print (j4)

"""
[1, "big", [1, "a", {"p": "+"}], [["t", 2], {"1": "o"}], {"c": 0, "d": 1}]
"""

# ------------------------------------------------------------------------------
# Tuple can be converted to JSON

tuple1 = (1, 0)
j5 = json.dumps(tuple1)
print (j5)

"""
[1, 0]
"""

# ------------------------------------------------------------------------------
# When we convert dictionary to JSON, key should be number or letter.
# Otherwise, we may get an error.
# We can use 'skipkeys' to skip these keys.

dic1 = {1:'one', 2.3:'tPt', 'two':2, (3,4):'thr&four'}
j6 = json.dumps(dic1)
print (j6)
# TypeError: keys must be a string

j7 = json.dumps(dic1, skipkeys = True)
print (j7)

"""
 {"1": "one", "2.3": "tPt", "two": 2}
"""
