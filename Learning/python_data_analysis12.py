import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

"""
output
"""
# Note: some output is shortened to save spaces.

# This file discusses variance analysis.

IS_t_test = pd.read_excel('E:\\IS_t_test.xlsx') 

Group1 = IS_t_test[IS_t_test['group']==1]['data']
Group2 = IS_t_test[IS_t_test['group']==2]['data']

# ------------------------------------------------------------------------------
# levene(*args, **kwds) Perform Levene test for equal variances.
# If p < 0.05, then variance not equal.

w,p = stats.levene(*args)

print (w,p)

"""
(0.019607843137254936, 0.89209916055865535)
"""

# ------------------------------------------------------------------------------
# Perform variance analysis

f,p = stats.f_oneway(*args)

"""
22.5771812081 0.00144238194084
"""

# ------------------------------------------------------------------------------
# multivariate analysis of variance (MANOVA)
# In statistics, MANOVA is a procedure for comparing multivariate sample means. 

MANOVA = pd.read_excel('E:\\MANOVA.xlsx')

"""
    id  nutrient  weight
0    1         1    50.1
1    2         1    47.8
2    3         1    53.1
3    4         1    63.5
4    5         1    71.2
5    6         1    41.4
.......................
21   6         3    38.5
22   7         3    51.2
23   8         3    46.2
"""

# ------------------------------------------------------------------------------
# multivariate analysis of variance (MANOVA)

formula = 'weight~C(id)+C(nutrient)+C(id):C(nutrient)'

anova_results = anova_lm(ols(formula,MANOVA).fit())
print (anova_results)

"""
                   df        sum_sq     mean_sq   F  PR(>F)
C(id)               7  2.373613e+03  339.087619   0     NaN
C(nutrient)         2  1.456133e+02   72.806667   0     NaN
C(id):C(nutrient)  14  3.391667e+02   24.226190   0     NaN
Residual            0  8.077936e-27         inf NaN     NaN
"""
