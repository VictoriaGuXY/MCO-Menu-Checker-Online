import pandas as pd

"""
output
"""
# Note: some output is shortened to save spaces.

# This file introduces how to extract and filter data we need (PART II).

df = pd.read_csv('E:\\tips.csv')

# We use the data from python_data_analysis1.py, which is:

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
# Suppose we only want data that tips > 8

print(df[df.tip>8])

"""
     total_bill  tip   sex smoker  day    time  size
170       50.81   10  Male    Yes  Sat  Dinner     3
212       48.33    9  Male     No  Sat  Dinner     4
"""

# ------------------------------------------------------------------------------
# Suppose we only want data that tips > 7 or total_bill > 50

print(df[(df.tip>7)|(df.total_bill>50)])

"""
     total_bill    tip   sex smoker  day    time  size
23        39.42   7.58  Male     No  Sat  Dinner     4
170       50.81  10.00  Male    Yes  Sat  Dinner     3
212       48.33   9.00  Male     No  Sat  Dinner     4
"""

# ------------------------------------------------------------------------------
# Suppose we only want data that tips > 7 and total_bill > 50

print(df[(df.tip>7)&(df.total_bill>50)])

"""
     total_bill  tip   sex smoker  day    time  size
170       50.81   10  Male    Yes  Sat  Dinner     3
"""

# ------------------------------------------------------------------------------
# Suppose we only want data that tips > 7 and total_bill > 50
# and we only cares about day and time

print (df[['day','time']][(df.tip>7)|(df.total_bill>50)])

"""
     day    time
23   Sat  Dinner
170  Sat  Dinner
212  Sat  Dinner
"""