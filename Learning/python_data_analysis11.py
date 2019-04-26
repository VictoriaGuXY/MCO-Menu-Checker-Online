import pandas as pd
from scipy.stats import ttest_rel

"""
output
"""
# Note: some output is shortened to save spaces.

# This file discusses statistical analysis (Part II).

# ------------------------------------------------------------------------------
# Data stored in form of xlsx with contents:

"""
   group  data
0      1    34
1      1    37
2      1    28
3      1    36
4      1    30
5      2    43
6      2    45
7      2    47
8      2    49
9      2    39
"""

# Assume these data are paired sample.

# ------------------------------------------------------------------------------

IS_t_test = pd.read_excel('E:\\IS_t_test.xlsx') 

Group1 = IS_t_test[IS_t_test['group']==1]['data']
Group2 = IS_t_test[IS_t_test['group']==2]['data']

print (ttest_rel(Group1,Group2))

"""
(-5.6873679190073361, 0.00471961872448184)
"""
# The first element from output is the value of t
# The second element from output is p-value
