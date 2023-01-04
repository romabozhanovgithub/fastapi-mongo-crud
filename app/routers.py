from bson import ObjectId
from fastapi import APIRouter, Depends
from motor.core import AgnosticCollection

from app.dependencies import get_db
from app.schemas import ItemResponse, ItemRequest

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/items/", response_model=ItemResponse)
async def create_item(
    item: ItemRequest, db: AgnosticCollection = Depends(get_db)
):
    res = await db.insert_one(item.dict())
    return {**item.dict(), "_id": res.inserted_id}


@router.get("/items/", response_model=list[ItemResponse])
async def read_items(db: AgnosticCollection = Depends(get_db)):
    items = await db.find().to_list(100)
    return list(items)


@router.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id: str, db: AgnosticCollection = Depends(get_db)):
    item = await db.find_one({"_id": ObjectId(item_id)})
    return item


@router.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(
    item: ItemRequest, item_id: str, db: AgnosticCollection = Depends(get_db)
):
    res = await db.update_one({"_id": ObjectId(item_id)}, {"$set": item.dict()})
    print(res)
    return {**item.dict(), "_id": item_id}


@router.delete("/items/{item_id}")
async def delete_item(item_id: str, db: AgnosticCollection = Depends(get_db)):
    await db.delete_one({"_id": ObjectId(item_id)})
    return {"message": "Item deleted"}
