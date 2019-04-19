import json

'''
output in comment
'''

# convert JSON into a Python dictionary or list using json.loads
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
py_text = json.loads(jsonData)
print (py_text)

'''  
{'a': 1, 'e': 5, 'b': 2, 'd': 4, 'c': 3}
'''


'''
NOTE:

{JSON} -> [Python]

{object} -> [dict]
{array} -> [list]
{string} -> [unicode]
{number(int)} -> [int,long]
{number(real)} -> [float]
{true} -> [True]
{false} -> [False]
{null} -> [None]
'''
