import pandas as pd

"""
output
"""
# Note: some output is shortened to save spaces.

# This file introduces methods to do descriptive statistics and sort the data
# based on a feature.

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
# descriptive statistics

print (df.describe())

"""
       total_bill         tip        size
count  244.000000  244.000000  244.000000
mean    19.785943    2.998279    2.569672
std      8.902412    1.383638    0.951100
min      3.070000    1.000000    1.000000
25%     13.347500    2.000000    2.000000
50%     17.795000    2.900000    2.000000
75%     24.127500    3.562500    3.000000
max     50.810000   10.000000    6.000000
"""

# ------------------------------------------------------------------------------
# Sorting the data based on tip

print(df.sort_values(by='tip'))

"""
     total_bill    tip     sex smoker   day    time  size
67         3.07   1.00  Female    Yes   Sat  Dinner     1
236       12.60   1.00    Male    Yes   Sat  Dinner     2
92         5.75   1.00  Female    Yes   Fri  Dinner     2
111        7.25   1.00  Female     No   Sat  Dinner     1
0         16.99   1.01  Female     No   Sun  Dinner     2
..          ...    ...     ...    ...   ...     ...   ...
214       28.17   6.50  Female    Yes   Sat  Dinner     3
141       34.30   6.70    Male     No  Thur   Lunch     6
59        48.27   6.73    Male     No   Sat  Dinner     4
23        39.42   7.58    Male     No   Sat  Dinner     4
212       48.33   9.00    Male     No   Sat  Dinner     4
170       50.81  10.00    Male    Yes   Sat  Dinner     3

[244 rows x 7 columns]
"""
