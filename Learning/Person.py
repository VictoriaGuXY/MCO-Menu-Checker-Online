# Person class is a class that defined by myself
# I will try to handle this custom type object and convert it to json.
# two ways to do this: see python_json4.py and python_json5.py

'''
output in comment
'''
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return 'Person Object name : %s , age : %d' % (self.name,self.age)
    
if __name__  == '__main__':
    p = Person('Peter',22)
    print (p)
    
    '''  
    Person Object name : Peter , age : 22
    '''  