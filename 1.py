import pymongo

# Connect to MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["clothes-db"]
collection = db["products"]

# Delete existing documents from the collection
collection.delete_many({})

# List of documents to insert
documents = [
    { "item": "blouse", "instock": [ { "size": "L", "qty": 15 }, { "size": "M", "qty": 35 }, { "size": "S", "qty": 25 } ], "type": "women" },
    { "item": "hoodie", "instock": [ { "size": "L", "qty": 20 }, { "size": "M", "qty": 25 }, { "size": "S", "qty": 30 } ], "type": "boys" },
    { "item": "jacket", "instock": [ { "size": "M", "qty": 20 }, { "size": "S", "qty": 30 } ], "type": "girls" },
    { "item": "jeans", "instock": [ { "size": "L", "qty": 30 }, { "size": "S", "qty": 20 } ], "type": "men" },
    { "item": "shirt", "instock": [ { "size": "M", "qty": 15 }, { "size": "S", "qty": 10 } ], "type": "women" }
]

# Insert documents into the collection
collection.insert_many(documents)

# 2-1. Find the total qty of each item and sort
pipeline = [
    {"$unwind": "$instock"},
    {"$group": {"_id": "$item", "total_qty": {"$sum": "$instock.qty"}}},
    {"$sort": {"total_qty": -1, "_id": 1}}
]
result_2_1 = list(collection.aggregate(pipeline))

# 2-2. Find the total inventory of each size and sort
pipeline = [
    {"$unwind": "$instock"},
    {"$group": {"_id": "$instock.size", "total_inventory": {"$sum": "$instock.qty"}}},
    {"$sort": {"total_inventory": -1}}
]
result_2_2 = list(collection.aggregate(pipeline))

# Display results
print("2-1. Total quantity of each item (sorted):")
for doc in result_2_1:
    print(f"{doc['_id']}: {doc['total_qty']}")

print("\n2-2. Total inventory of each size (sorted):")
for doc in result_2_2:
    print(f"{doc['_id']}: {doc['total_inventory']}")

