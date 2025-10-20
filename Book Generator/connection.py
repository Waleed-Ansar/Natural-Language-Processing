from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb+srv://Waleed-Ansar:fastAPI%40waleed570@fastapi-cluster.0yfuiu4.mongodb.net/")
db = client["Book_Shelf"]
collection_name = db['Books']
api_keys = db['api_key']
