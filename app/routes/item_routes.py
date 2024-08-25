from fastapi import APIRouter, HTTPException, Depends, status
from app.schemas import ItemCreate, ItemResponse, ItemUpdate
from app.services import ItemService

router = APIRouter()


@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item_create: ItemCreate, item_service: ItemService = Depends()):
    """
    Create a new item.

    Args:
        item_create (ItemCreate): The item data to create.
        item_service (ItemService): The service handling item logic.

    Returns:
        ItemResponse: The created item with its ID.
    """
    item = await item_service.create_item(item_create)
    return ItemResponse(id=str(item["_id"]), **item)


@router.get("/{item_id}", response_model=ItemResponse)
async def read_item(item_id: str, item_service: ItemService = Depends()):
    """
    Get an item by ID.

    Args:
        item_id (str): The ID of the item to retrieve.
        item_service (ItemService): The service handling item logic.

    Returns:
        ItemResponse: The requested item.

    Raises:
        HTTPException: If the item is not found.
    """
    item = await item_service.get_item(item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return ItemResponse(id=str(item["_id"]), **item)


@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(
    item_id: str, item_update: ItemUpdate, item_service: ItemService = Depends()
):
    """
    Update an item by ID.

    Args:
        item_id (str): The ID of the item to update.
        item_update (ItemUpdate): The updated item data.
        item_service (ItemService): The service handling item logic.

    Returns:
        ItemResponse: The updated item.

    Raises:
        HTTPException: If the item is not found.
    """
    updated_item = await item_service.update_item(item_id, item_update)
    if updated_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return ItemResponse(id=str(updated_item["_id"]), **updated_item)


@router.delete("/{item_id}", response_model=ItemResponse)
async def delete_item(item_id: str, item_service: ItemService = Depends()):
    """
    Delete an item by ID.

    Args:
        item_id (str): The ID of the item to delete.
        item_service (ItemService): The service handling item logic.

    Returns:
        ItemResponse: The deleted item.

    Raises:
        HTTPException: If the item is not found.
    """
    deleted_item = await item_service.delete_item(item_id)
    if deleted_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return ItemResponse(id=str(deleted_item["_id"]), **deleted_item)
