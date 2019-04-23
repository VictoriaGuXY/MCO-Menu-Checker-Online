import json

"""
output
"""

# This file contains notes of how to save a JSON file and read a JSON file.

# ------------------------------------------------------------------------------
# To convert a Python object and save as a JSON file, we should use dump
# instead of dumps.

dic_info = {'name':'Elizabeth', 'husband':'daxi', 'age':22}
filew = open ('Elizabeth.json', 'w', encoding='utf-8')
json.dump(dic_info, filew)
filew.close()

# ------------------------------------------------------------------------------
# When should we use dumps?
# Example: convert a list to JSON

list1 = [1, 'big', [1, 'a', {'p':'+'}], (['t',2],{'1':'o'}), {'c':0,'d':1}]
j1 = json.dumps(list1)
print (j1)

""" 
[1, "big", [1, "a", {"p": "+"}], [["t", 2], {"1": "o"}], {"c": 0, "d": 1}]
"""

# ------------------------------------------------------------------------------
# To read a JSON file and save it as a Python object, we should use load 
# instead of loads.

filer = open ('Elizabeth.json', 'r', encoding='utf-8')
Elizabeth = json.load(filer)
filer.close()
print (Elizabeth)
"""
{'name': 'Elizabeth', 'husband': 'daxi', 'age': 22}
"""

print (type(Elizabeth))
"""
<class 'dict'>
"""

# ------------------------------------------------------------------------------
# When should we use loads?
# Example: convert a JSON to Python typed object

dic = {'b':'I', 'a':123, 'c':'100'}
j2 = json.dumps(dic)
decode1 = json.loads(j2)
print (decode1)

""" 
{'b': 'I', 'a': 123, 'c': '100'}
"""
