import pyodbc

conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=cafee-demo.database.windows.net;DATABASE=cafe;UID=cafe-admin;PWD=sinha@2024')
cursor = conn.cursor()

print("Connected")