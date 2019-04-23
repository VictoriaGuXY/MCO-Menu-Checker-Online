from json import *

"""
output
"""

# This file contains the use of JSONEncoder and JSONDecoder, as an aid to
# python_json5.py.

# In this program, 
# JSONEncoder() converts a Python dict type to a JSON string.
# JSONDecoder() converts a JSON string to a Python dict type.

if __name__=="__main__":   
   d={}
   d['a'] =1
   d['b']=2
   d[3]='c'
   d[4]=['k','k1']  
   # JSONEncoder() converts a Python dict type to a JSON string.
   k=JSONEncoder().encode(d)
   print(type(k))
   print(k)
   # JSONDecoder() converts a JSON string to a Python dict type.
   json_str='{"a":1,"b":2,"3":"c","4":["k","k1"]}'
   d=JSONDecoder().decode(json_str)
   print(type(d))
   print(d)
   
"""
<class 'str'>
{"4": ["k", "k1"], "3": "c", "a": 1, "b": 2}
<class 'dict'>
{'3': 'c', 'a': 1, 'b': 2, '4': ['k', 'k1']}
"""

# Note:
# To have a correct output, we have to use (") to represent a JSON string
# instead of using ('). 
# If we use ('), then we may get an error when we try to convert JSON string
# to Python dict.
