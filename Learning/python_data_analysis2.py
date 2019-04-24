import pandas as pd
import MySQLdb

"""
output
"""

# This file introduces method to read Mysql data.

# Suppose we have the data saved locally. 
# Suppose the username is myusername and passowrd is mypassword.
# We want to read data saved in mydb.

mysql_cn= MySQLdb.connect(host = 'localhost', port = 3306,user = 'myusername', passwd = 'mypassword', db = 'mydb')
df = pd.read_sql('select * from test;', con = mysql_cn)    
mysql_cn.close()

# The above code reads all data from test to df.
# The data type of df is Dataframe.

# More on http://www.runoob.com/mysql/mysql-tutorial.html
