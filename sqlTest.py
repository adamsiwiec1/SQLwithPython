import pd as pd
from config import sqlConnection

cursor = sqlConnection.cursor()

cursor.execute('SELECT * from TestTable')

for row in cursor:
    print(row)
