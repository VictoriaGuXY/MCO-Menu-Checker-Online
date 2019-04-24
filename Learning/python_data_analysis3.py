import pandas as pd
import sqlite3

"""
output
"""

# This file introduces method to read and write an SQL

con = sqlite3.connect('...')
sql = '...'
df = pd.read_sql(sql,con)

# ------------------------------------------------------------------------------
# help file
help(sqlite3.connect)

"""
Help on built-in function connect in module _sqlite3:

connect(...)
    connect(database[, timeout, isolation_level, detect_types, factory])
    
    Opens a connection to the SQLite database file *database*. You can use
    ":memory:" to open a database connection to a database that resides in
    RAM instead of on disk.
"""

# ------------------------------------------------------------------------------
# help file
help(pd.read_sql)

"""
Help on function read_sql in module pandas.io.sql:

read_sql(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None, chunksize=None)
    Read SQL query or database table into a DataFrame.
"""
