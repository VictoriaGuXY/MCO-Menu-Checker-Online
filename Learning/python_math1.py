sudo pip install sympy
from sympy import *

"""
output
"""

# This file introduces how to do math in python.

#-------------------------------------------------------------------------------
# Solve basic function

print (solve(x * 3 - 6, x))

"""
[3]
"""

#-------------------------------------------------------------------------------
# Solve equation set

x=Symbol('x')
y=Symbol('y')
print (solve([y+x-1,3*x+2*y-5],[x,y]))

"""
{x: 3, y: -2}
"""

#-------------------------------------------------------------------------------
# find limit

x = Symbol('x')
print (limit(1/x**2, x, 0))

"""
oo
"""

x = Symbol('x')
print (limit(x*(sqrt(x**2 + 1) - x), x, oo))

"""
1/2
"""

# a harder one
x = Symbol('x')
pprint(x*(sqrt(x**2 + 1) - x))

#-------------------------------------------------------------------------------
# find integration

n = Symbol('n')
s = ((n+3)/(n+2))**n
print (limit(s, n, oo))

"""
E
"""

t = Symbol('t')
x = Symbol('x')
m = integrate(sin(t)/(pi-t),(t,0,x))
n = integrate(m,(x,0,pi))
print (n)

"""
2
"""
