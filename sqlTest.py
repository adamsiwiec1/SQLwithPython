import pandas as pd
from config import sqlConnection

cursor = sqlConnection.cursor()
cursor.execute('SELECT * FROM TestTable')

for row in cursor:
    print(row)
