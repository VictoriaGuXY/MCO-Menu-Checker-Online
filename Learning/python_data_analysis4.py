import pandas as pd

"""
output
"""
# Note: some output is shortened to save spaces.

# This file introduces how to extract and filter data we need (PART I).

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
# extract and read corresponding data
# print first five lines
print (df.head())

"""
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
"""

# ------------------------------------------------------------------------------
# print first five lines
print (df.tail())

"""
     total_bill   tip     sex smoker   day    time  size
239       29.03  5.92    Male     No   Sat  Dinner     3
240       27.18  2.00  Female    Yes   Sat  Dinner     2
241       22.67  2.00    Male    Yes   Sat  Dinner     2
242       17.82  1.75    Male     No   Sat  Dinner     2
243       18.78  3.00  Female     No  Thur  Dinner     2
"""

# ------------------------------------------------------------------------------
# print the column names
print (df.columns)

"""
Index([u'total_bill', u'tip', u'sex', u'smoker', u'day', u'time', u'size'], dtype='object')
"""

# ------------------------------------------------------------------------------
# print the line names
print (df.index)

"""
Int64Index([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,
            ...
            234, 235, 236, 237, 238, 239, 240, 241, 242, 243],
           dtype='int64', length=244)
"""

# ------------------------------------------------------------------------------
# print the data from first 3 columns of first 10-20 lines
print (df.ix[10:20, 0:3])

"""
    total_bill   tip     sex
10       10.27  1.71    Male
11       35.26  5.00  Female
12       15.42  1.57    Male
13       18.43  3.00    Male
14       14.83  3.02  Female
15       21.58  3.92    Male
16       10.33  1.67  Female
17       16.29  3.71    Male
18       16.97  3.50  Female
19       20.65  3.35    Male
20       17.92  4.08    Male
"""

# ------------------------------------------------------------------------------
# extract the data from not consecutive lines or columns
# Example: data from columns 1,3,5, line 2,4
print (df.iloc[[1,3,5],[2,4]])

"""
    sex  day
1  Male  Sun
3  Male  Sun
5  Male  Sun
"""

# ------------------------------------------------------------------------------
# extract a specific data
# Example: data from line 3, column 2
print (df.iat[3,2])

"""
'Male'
"""

# ------------------------------------------------------------------------------
# ingore first 2 columns
print (df.drop(df.columns[1, 2], axis = 1))

# ingore first 2 rows
print (df.drop(df.columns[[1, 2]], axis = 0))

# ------------------------------------------------------------------------------
# print the dimensions of data frame
print (df.shape)

"""
(244, 7)
"""
