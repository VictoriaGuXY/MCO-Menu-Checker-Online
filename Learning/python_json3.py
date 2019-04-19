import json

# use library Demjson
# Github: https://github.com/dmeranda/demjson
# official website: http://deron.meranda.us/python/demjson/
import demjson 

'''
output in comment
'''

# Python can use demjson.encode() method to parse Python object into JSON
# demjson.encode(self, obj, nest_level=0)

py_data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
json_str = demjson.encode(py_data)
print (json_str)

'''
[{"a":1,"b":2,"c":3,"d":4,"e":5}]
'''


# demjson.decode() method decodes a JSON-encoded string into a Python object
# demjson.decode(self, txt)

json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
py_text = demjson.decode(json)
print (py_text)

'''
{u'a': 1, u'c': 3, u'b': 2, u'e': 5, u'd': 4}
'''
