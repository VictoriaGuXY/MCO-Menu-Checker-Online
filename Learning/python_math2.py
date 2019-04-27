from sympy import *
"""
output
"""
# This file introduces different ways to solve functions in Python.

#-------------------------------------------------------------------------------
# using sympy

x = symbols('x')
y = symbols('y')
res = solve([x+y-3,x-y-1],[x,y])[0]

#-------------------------------------------------------------------------------
# using sage: quick

var('x y')
solve([x**3+y**2+666==142335262,x**2-y==269086,x+y==1834],[x,y])

#-------------------------------------------------------------------------------
# using z3

Int('x')
Real('x')
Bool('x')
BitVec('x',N) # N bit
BitVecVal(num,N)

# initialization
solver = Solver()
solver.add(x+y==10,x-y==0)
solver.check()
ans = solver.mode()

# initialization
x = [Int('x%d' % i) for i in range(n)]
# get a value
value = ans[x].as_long()
