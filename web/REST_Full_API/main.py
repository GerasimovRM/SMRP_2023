from enum import Enum
from typing import List

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from endpoints import student_router


app = FastAPI()
app.include_router(student_router)


class ItemDtoIn(BaseModel):
    name: str
    price: float


class ItemDtoOut(ItemDtoIn):
    id: int

# item: id, name, price
fake_db_item_id = 3
fake_db = {"items":[
    ItemDtoOut(id=1, name='54656754', price=657657),
    ItemDtoOut(id=2, name='fdgfd', price=657),
    ItemDtoOut(id=3, name='657', price=123)
]}




class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.post("/items", response_model=ItemDtoOut)
async def create_item(item: ItemDtoIn):
    global fake_db_item_id
    fake_db_item_id += 1
    # new_item = ItemDtoOut(id=fake_db_item_id,
    #                       name=item.name,
    #                       price=item.price)
    new_item = ItemDtoOut(id=fake_db_item_id,
                          **item.dict())
    fake_db["items"].append(new_item)
    return new_item


@app.get("/items/{item_id}", response_model=ItemDtoOut)
async def get_one(item_id: int):
    for item in fake_db["items"]:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404,
                        detail="Item not found")


@app.get("/items", response_model=List[ItemDtoOut])
async def get_all():
    return fake_db["items"]


@app.put("/items/{item_id}", response_model=ItemDtoOut)
async def put_item(item_id: int,
                   item_dto: ItemDtoIn):
    for i, item in enumerate(fake_db["items"]):
        if item.id == item_id:
            new_item = ItemDtoOut(id=item.id, **item_dto.dict())
            fake_db["items"][i] = new_item
            return new_item
    raise HTTPException(status_code=404,
                        detail=f"Item {item_id} not found")


@app.delete("/items/{item_id}")
async def put_item(item_id: int):
    for i, item in enumerate(fake_db["items"]):
        if item.id == item_id:
            fake_db["items"].pop(i)
            return {"status": "ok"}
    raise HTTPException(status_code=404,
                        detail=f"Item {item_id} not found")


if __name__ == "__main__":
    uvicorn.run("web.REST_Full_API.main:app",
                host="127.0.0.1",
                port=5000,
                log_level="info",
                reload=True)
