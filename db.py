import pyodbc

# server name: DESKTOP-7DF645S\SQLEXPRESS

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-7DF645S\SQLEXPRESS;DATABASE=cafe;')

# Using a DSN, but providing a password as well
#conn = pyodbc.connect('DSN=test;PWD=password')

# Create a cursor from the connection
cursor = conn.cursor()

print("db connected")

cursor.execute("select * from item")
rows = cursor.fetchall()

for row in rows:
    #print("row ---> ",row)
    print(f"id = {row[0]}, name = {row[1]}, price = {row[2]}",)
    # print("row.type ---> ",type(row))

# items = [
#     {
#         "name": "mango",
#         "price": 120,
#         "inventory"  : True
#     },
#     {
#         "name": "banana",
#         "price": 80,
#         "inventory"  : False
#     }
# ]

# print("Hello pytondb.")
# print("items",items)