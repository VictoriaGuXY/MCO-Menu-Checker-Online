import pandas as pd

# pandas provides us lots of data frame and functions that we can quickly use
# to analyze data.

"""
output
"""

# This file contains notes of basic data analyzing strategies using Python.
# I will introduce two ways to read a csv file: pathway and URL.
# Also, I will introduce how to output data and save them into a csv file.

# ------------------------------------------------------------------------------
# read a csv file using the pathway
# This is based on the pathway that we saved the file.
# In python, to represent a pathway, we should either use / or //.

df = pd.read_csv('E:\\tips.csv')

# ------------------------------------------------------------------------------
# read data online using a URL

data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv" 
df = pd.read_csv(data_url)

# same output for the above two methods
# output is shown below
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
# output data and save them into a csv file

df.to_csv('E:\\demo.csv', encoding='utf-8', index=False) 

# When index = False, when output as a csv file, the name of each line will be
# removed.
# If we contain some special characters in data, encoding will treat it as 
# utf-8.
