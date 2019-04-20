import Person
import json

'''
output in comment
'''

# We cannot directly use json.dump to convert a custom type.
# To use json.dump, we have to convert the Person type into dict type.
# Here comes my first method to do this. The other method is displayed in python_json5.py.
# This method is basically to write my own method of convertion.

p = Person.Person('Peter',22)
 
def object2dict(obj):
    # convert object to a dict
    d = {}
    d['__class__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    return d
 
def dict2object(d):
    # convert dict to object
    if'__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module,class_name)
        args = dict((key.encode('ascii'), value) for key, value in d.items()) # get args
        inst = class_(**args) # create new instance
    else:
        inst = d
    return inst
 
d = object2dict(p)
print (d)

'''  
{'age': 22, '__module__': 'Person', '__class__': 'Person', 'name': 'Peter'}
'''  
 
o = dict2object(d)
print (type(o),o)

'''  
<class 'Person.Person'> Person Object name : Peter , age : 22
 '''  
# use json.dumps to get json
dump = json.dumps(p,default=object2dict)
print (dump)

'''  
{"age": 22, "__module__": "Person", "__class__": "Person", "name": "Peter"}
 '''  

# use json.loads
load = json.loads(dump,object_hook = dict2object)
print (load)

'''  
Person Object name : Peter , age : 22
'''  
