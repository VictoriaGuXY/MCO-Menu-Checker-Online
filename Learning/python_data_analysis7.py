import json
import pandas as pd
import numpy as np
from pandas import DataFrame

"""
output
"""
# Note: some output is shortened to save spaces.

# This file introduces methods to deal with the missing values.

path = 'F:\PycharmProjects\pydata-book-master\ch02\usagov_bitly_data2012-03-16-1331923249.txt' 
records = [json.loads(line) for line in open(path)]
frame = DataFrame(records)
frame['tz']

"""
0          America/New_York
1            America/Denver
2          America/New_York
3         America/Sao_Paulo
4          America/New_York
5          America/New_York
6             Europe/Warsaw
7                          
8                          
9                          
10      America/Los_Angeles
11         America/New_York
12         America/New_York
13                      NaN
               ...         
Name: tz, dtype: object
"""

# From the above output, we can see some values are missing and unknown.
# We have strategies to deal with this case.

# ------------------------------------------------------------------------------
# use numbers to replace missing values

print (frame['tz'].fillna(1111111111111))

"""
0          America/New_York
1            America/Denver
2          America/New_York
3         America/Sao_Paulo
4          America/New_York
5          America/New_York
6             Europe/Warsaw
7                          
8                          
9                          
10      America/Los_Angeles
11         America/New_York
12         America/New_York
13            1111111111111
Name: tz, dtype: object
"""

# ------------------------------------------------------------------------------
# use strings to replace missing values

print (frame['tz'].fillna('XXXXXXXXXXXXXXXXXX'))

"""
0          America/New_York
1            America/Denver
2          America/New_York
3         America/Sao_Paulo
4          America/New_York
5          America/New_York
6             Europe/Warsaw
7                          
8                          
9                          
10      America/Los_Angeles
11         America/New_York
12         America/New_York
13       XXXXXXXXXXXXXXXXXX
Name: tz, dtype: object
"""


# ------------------------------------------------------------------------------
# use the value right before the missing value to replace it
print (frame['tz'].fillna(method='pad'))

# use the value right after the missing value to replace it
print (frame['tz'].fillna(method='bfill'))

# ------------------------------------------------------------------------------
# delete the missing value
# delete the missing line
print (frame['tz'].dropna(axis=0))

# delete the missing column
print (frame['tz'].dropna(axis=1))
