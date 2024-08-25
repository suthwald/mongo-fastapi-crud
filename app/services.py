import logging
from fastapi import HTTPException
from app.models import ItemModel
from app.schemas import ItemCreate, ItemUpdate

logger = logging.getLogger(__name__)

class ItemService:
    @staticmethod
    async def create_item(item_create: ItemCreate):
        try:
            item_dict = item_create.dict()
            item = await ItemModel.create(item_dict)
            logger.info(f"Item created: {item}")
            return item
        except Exception as e:
            logger.error(f"Error creating item: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")

    @staticmethod
    async def get_item(item_id: str):
        item = await ItemModel.find(item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    @staticmethod
    async def update_item(item_id: str, item_update: ItemUpdate):
        update_dict = item_update.dict(exclude_unset=True)
        item = await ItemModel.update(item_id, update_dict)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    @staticmethod
    async def delete_item(item_id: str):
        item = await ItemModel.delete(item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item
