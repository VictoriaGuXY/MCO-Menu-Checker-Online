import pandas as pd
import numpy as np

"""
output
"""
# Note: some output is shortened to save spaces.

# This file discusses data substitution.

# ------------------------------------------------------------------------------
# first of all, we create a series
Series = pd.Series([0,1,2,3,4,5])

"""
Series
0    0
1    1
2    2
3    3
4    4
5    5
dtype: int64
"""

# ------------------------------------------------------------------------------
# then, we substitute 0 with 10000000000000

print (Series.replace(0,10000000000000))

"""
0    10000000000000
1                 1
2                 2
3                 3
4                 4
5                 5
dtype: int64
"""

# ------------------------------------------------------------------------------
# Similarly, we can also do substitution of columns.

print (Series.replace([0,1,2,3,4,5],[11111,222222,3333333,44444,55555,666666]))

"""
0      11111
1     222222
2    3333333
3      44444
4      55555
5     666666
dtype: int64
"""
