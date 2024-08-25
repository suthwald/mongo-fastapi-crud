from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str
    price: float
    in_stock: bool

class ItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    in_stock: bool | None = None

class ItemResponse(BaseModel):
    id: str
    name: str
    description: str
    price: float
    in_stock: bool

    class Config:
        from_attributes = True  # Updated for Pydantic v2
