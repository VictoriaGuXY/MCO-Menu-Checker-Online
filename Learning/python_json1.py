import json

'''
output in comment
'''

# convert array into json using json.dumps
data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
json = json.dumps(data)
print(json)

'''  
[{"a": 1, "c": 3, "b": 2, "e": 5, "d": 4}]
'''


# formatted output
print(json.dumps({'a': 'xxx', 'b': 7}, sort_keys = True, indent = 4, separators = (',', ': ')))

'''
{
    "a": "xxx",
    "b": 7
}
'''


'''
NOTE:

[Python] -> {JSON}

[dict] -> {object}
[list,tuple] -> {array}
[str,unicode] -> {string}
[int,long,float] -> {number}
[True] -> {true}
[False] -> {false}
[None] -> {null}
'''
