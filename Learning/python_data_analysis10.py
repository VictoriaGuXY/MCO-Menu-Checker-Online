import pandas as pd
from scipy.stats import ttest_ind

"""
output
"""
# Note: some output is shortened to save spaces.

# This file discusses statistical analysis (Part I).

# ------------------------------------------------------------------------------
# first of all, some background knowledge about Student's t-test

'''
The t-test is any statistical hypothesis test in which the test statistic follows 
a Student's t-distribution under the null hypothesis.

A t-test is most commonly applied when the test statistic would follow a normal 
distribution if the value of a scaling term in the test statistic were known. 
When the scaling term is unknown and is replaced by an estimate based on the data, 
the test statistics (under certain conditions) follow a Student's t distribution. 
The t-test can be used, for example, to determine if the means of two sets of data 
are significantly different from each other.
(from Wikipedia)
'''

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

IS_t_test = pd.read_excel('E:\\IS_t_test.xlsx') 

Group1 = IS_t_test[IS_t_test['group']==1]['data']
Group2 = IS_t_test[IS_t_test['group']==2]['data']

print (ttest_ind(Group1,Group2))

"""
(-4.7515451390104353, 0.0014423819408438474) 
"""

# The first element from output is the value of t
# The second element from output is p-value

# ------------------------------------------------------------------------------
# ttest_ind assumes that two sets of data have the same variance.
# If we want them to have different variances, we can set equal_var=False.

print (ttest_ind(Group1,Group2,equal_var=True))
print (ttest_ind(Group1,Group2,equal_var=False))

"""
(-4.7515451390104353, 0.0014423819408438474)
(-4.7515451390104353, 0.0014425608643614844)
"""
