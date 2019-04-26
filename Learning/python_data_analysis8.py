import json
import pandas as pd
import numpy as np
from pandas import DataFrame

"""
output
"""
# Note: some output is shortened to save spaces.

# This file introduces methods to group data.

# Data from https://github.com/mwaskom/seaborn-data
df = pd.read_csv('E:\\tips.csv')

"""
     total_bill   tip     sex smoker   day    time  size
0         16.99  1.01  Female     No   Sun  Dinner     2
1         10.34  1.66    Male     No   Sun  Dinner     3
2         21.01  3.50    Male     No   Sun  Dinner     3
3         23.68  3.31    Male     No   Sun  Dinner     2
4         24.59  3.61  Female     No   Sun  Dinner     4
5         25.29  4.71    Male     No   Sun  Dinner     4
..          ...   ...     ...    ...   ...     ...   ...
240       27.18  2.00  Female    Yes   Sat  Dinner     2
241       22.67  2.00    Male    Yes   Sat  Dinner     2
242       17.82  1.75    Male     No   Sat  Dinner     2
243       18.78  3.00  Female     No  Thur  Dinner     2
[244 rows x 7 columns]
"""

# ------------------------------------------------------------------------------
# if we want to form group based on 'day' column

group = df.groupby('day')

# print out the first value (first line) in each group
print (group.first())

"""
      total_bill   tip     sex smoker    time  size
day                                                
Fri        28.97  3.00    Male    Yes  Dinner     2
Sat        20.65  3.35    Male     No  Dinner     3
Sun        16.99  1.01  Female     No  Dinner     2
Thur       27.20  4.00    Male     No   Lunch     4
"""

# print out the last value (last line) in each group
print (group.first())

"""
      total_bill   tip     sex smoker    time  size
day                                                
Fri        10.09  2.00  Female    Yes   Lunch     2
Sat        17.82  1.75    Male     No  Dinner     2
Sun        15.69  1.50    Male    Yes  Dinner     2
Thur       18.78  3.00  Female     No  Dinner     2
"""
