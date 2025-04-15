from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple API")

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Simple API"}

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item, "total_price": item.price + (item.tax or 0)} 