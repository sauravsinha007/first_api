import uuid
import pyodbc

class ItemDatabase:
    def __init__(self):
        #--- Server Connection ------
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=cafe-test-sa.database.windows.net;DATABASE=cafe;UID=cafe-admin;PWD=sinha@2024')
        # ---- Local Host -----
        #self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-7DF645S\SQLEXPRESS;DATABASE=cafe;')
        # Using a DSN, but providing a password as well
        #conn = pyodbc.connect('DSN=test;PWD=password')
        # Create a cursor from the connection
        self.cursor = self.conn.cursor()
        print("db connected")

    def getItemsFromDb(self):
        query = "SELECT * FROM item"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        result = []
        for row in rows:
            item_dict = {}
            item_dict["id"] = row[0]
            item_dict["name"] = row[1]
            item_dict["price"] = row[2]
            result.append(item_dict)

        print(result)
        return result

    def getItemFromDb(self, item_name):
        query = "SELECT * FROM item where name = '" + item_name + "'"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        result = []
        for row in rows:
            item_dict = {}
            item_dict["id"] = row[0]
            item_dict["name"] = row[1]
            item_dict["price"] = row[2]
            result.append(item_dict)

        print(result)
        return result

    def addItemInDb(self,id,bodyObject):
        print(f"id  = {id} ---- bodyObject = {bodyObject}")
        name = bodyObject["name"]
        price = bodyObject["price"]
        query = "insert into item (id,name,price) values "
        query += "('" + str(id) + "', "
        query += "'" + name + "', "
        query +=  str(price) + ")"
        print("query = ",query)
        result = self.cursor.execute(query)
        effectRow = self.cursor.rowcount
        print(f"rowCount = {effectRow}")
        #print(f"result = {result} --- {result.messages}")
        if effectRow == 0:
            return False
        else:
            self.conn.commit()
            return True   

    def updateItemInDb(self,bodyObject):
        print(f"bodyObject = {bodyObject}")
        itemId = str(bodyObject["id"])
        name = bodyObject["name"]
        price = str(bodyObject["price"])
        query = "UPDATE item SET "
        if len(name) > 0:
            query += "name = '" + name + "'" 

        if len(name) > 0 and len(price) > 0:
             query += " , "

        if len(price) > 0:
            query += "price = " + price   
        
        query += " WHERE id = '" + itemId + "'"
        print("query = ",query)

        result = self.cursor.execute(query)
        effectRow = self.cursor.rowcount
        print(f"rowCount = {effectRow}")
        #print(f"result = {result} --- {result.messages}")
        if effectRow == 0:
            return False
        else:
            self.conn.commit()
            return True     

    def deleteItemFromDb(self,bodyObject):
        print(f"bodyObject = {bodyObject}")
        itemId = str(bodyObject["id"])
        query = "DELETE FROM item "        
        query += " WHERE id = '" + itemId + "'"
        print("query = ",query)
        result = self.cursor.execute(query)
        effectRow = self.cursor.rowcount
        print(f"rowCount = {effectRow}")
        #print(f"result = {result} --- {result.messages}")
        if effectRow == 0:
            return False
        else:
            self.conn.commit()
            return True  
        
#         insert into item (id, name, price) values 
# ('1234abcd45', 'Mango Shake', 120),
# ('12321aaaa5','Banana Shake',80)

#db = ItemDatabase()

# unique_id = uuid.uuid4()
# print(f"unique_id type =  {type(unique_id)}")
# itemDict = {
#                 "name": "Orange Juice1",
#                 "price": 60,
#                 "id": '7b5313e8-1bc4-4ea0-8d03-713d7ea5a342'
#             }
# itemDict = {
#                 "id": '7b5313e8-1bc4-4ea0-8d03-713d7ea5a342'
#             }
# db.deleteItemFromDb(itemDict)
#db.updateItemInDb(itemDict)
# db.addItemInDb(unique_id, itemDict)
#    db.getItemsFromDb()



