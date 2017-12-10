from __future__ import print_function
import sqlite3
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import style
# style.use('fivethirtyeight')

"""Show changes between two database tables.
However, Index numbers are not considered for comparision"""


db1_file = "dbs/db1.sqlite3"
db2_file = "dbs/db2.sqlite3"
con1 = sqlite3.connect(db1_file)
con2 = sqlite3.connect(db2_file)

df1 = pd.read_sql('SELECT * FROM web_stat', con=con1)
df2 = pd.read_sql('SELECT * FROM web_stat', con=con2)

# ne = (df1 != df2).any(1)
ne_stacked = (df1 != df2).stack()
changed = ne_stacked[ne_stacked]
changed.index.names = ['idx', 'col']

difference_locations = np.where(df1 != df2)
changed_from = df1.values[difference_locations]
changed_to = df2.values[difference_locations]

df_diff = pd.DataFrame({'from': changed_from, 'to': changed_to}, index=changed.index)
print(df_diff)

con1.close()
con2.close()
