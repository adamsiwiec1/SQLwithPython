import pyodbc

sqlConnection = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-FMRK48D\SQLSERVER2019;'
                      'Database=PythonTest;'
                      'Trusted_Connection=yes;')

