import uuid
from flask import Flask, request
#from db import items
from itemDb import ItemDatabase

app =  Flask(__name__)
db = ItemDatabase()
# items = [
#  
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

# http://127.0.0.1:5000

# http://127.0.0.1:5000/get-items

# get method
@app.get('/get-items')
def get_items():
    return db.getItemsFromDb()
    #return {"items" : items}

#Dynamic url
@app.get('/get-item/<string:name>')
def get_item(name):
    return db.getItemFromDb(name)

# Post 
@app.post('/add-item')
def add_item():
    request_data = request.get_json()
    unique_id = uuid.uuid4()
    print("request_data = ",request_data)
    db.addItemInDb(unique_id,request_data)
    return {"message": "item added sucessfully"}

@app.post('/update-item')
def update_item():
    request_data = request.get_json()
    print("request_data = ",request_data)
    db.updateItemInDb(request_data)
    return {"message": "item updated sucessfully"}

@app.post('/delete-item')
def delete_item():
    request_data 
    = request.get_json()
    print("request_data = ",request_data)
    db.deleteItemFromDb(request_data)
    return {"message": "item deleted sucessfully"}

#     return {"message":"Item not exist"}

# # Query Parameter
# @app.get('/get-item-query-parameter')
# def get_item_query_parameter():
#     name = request.args.get('name')
#     for item in items:
#         if item["name"] == name:
#             return {"item" : item}
        
#     return {"message":"Item not exist"}

# # Post 
# @app.post('/add-item')
# def add_item():
#     request_data = request.get_json()
#     #print(request_data)
#     items.append(request_data)
#     return {"message": "item added sucessfully"}