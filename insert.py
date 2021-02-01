import pd as pd
from termcolor import colored
from config import sqlConnection
import pandas as pd
import sqlite3

cursor = sqlConnection.cursor()

# Create Command
sqlCommand = ("""INSERT INTO Stock(Ticker, Price, Ask, Bid, DayLow, DayHigh, Volume, MarketOpen, MarketClose)
                            values ('TEST', 6.99, 6.99, 6.99,6.99, 6.99, 100, 6.99, 6.99)""")
try:
    # Execute SQL Command
    cursor.execute(sqlCommand)

    # Commit Changes to SQL Database
    sqlConnection.commit()
except Exception as e:
    print(colored(e, "red"))
    # Roll back in case of error
    sqlConnection.rollback()

selectStocks = "SELECT * FROM Stock"

try:
    # Execute SQL Command
    cursor.execute(selectStocks)

    # Print it
    for row in cursor:
        print(row)

except Exception as e:
    print(colored(e, "red"))
    # Roll back in case of error
    sqlConnection.rollback()


# Close SQL Connection
sqlConnection.close()


# cursor.execute('SELECT * from Stock;')
#
# for row in cursor:
#     print(row)
