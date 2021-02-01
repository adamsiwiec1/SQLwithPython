import pandas as pd
from config import sqlConnection

sql_query = pd.read_sql_query('SELECT * FROM TestTable', sqlConnection)
print(sql_query)
print(type(sql_query))