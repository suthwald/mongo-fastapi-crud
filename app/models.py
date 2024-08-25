from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from app.config import settings

client = AsyncIOMotorClient(settings.mongodb_url)
db = client[settings.database_name]
items_collection = db["items"]

class ItemModel:
    @staticmethod
    async def create(item_dict):
        result = await items_collection.insert_one(item_dict)
        return await items_collection.find_one({"_id": result.inserted_id})

    @staticmethod
    async def find(item_id):
        return await items_collection.find_one({"_id": ObjectId(item_id)})

    @staticmethod
    async def update(item_id, update_dict):
        result = await items_collection.update_one(
            {"_id": ObjectId(item_id)},
            {"$set": update_dict}
        )
        if result.matched_count == 0:
            return None
        return await items_collection.find_one({"_id": ObjectId(item_id)})

    @staticmethod
    async def delete(item_id):
        return await items_collection.find_one_and_delete({"_id": ObjectId(item_id)})
