from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
item_mobile = {
    1: {"Mobile": "Redmi", "gpu": "Snapdragon 690"},
    2: {"Mobile": "Realme", "gpu": "Snapdragon 6 gen 4"},
    3: {"Mobile": "Motorola", "gpu": "Snapdragon 7 gen 3"},
    4: {"Mobile": "Iqoo", "gpu": "Snapdragon 8 gen 4"},
}

@app.get("/")
def read_root():
    return {"message": "Hello World", "status": "running"}

@app.get("/about")
def about():
    return {"project": "My First API", "author": "Aayush Raj"}

@app.get("/items/laptop")
def items(id):
    return {"laptop": "ColorFul","gpu": "RTX 4060"}
@app.get("/item/mobile/{id}")
def mobile(id: int):
    return item_mobile.get(id,{"error": "Item not found"})

@app.post("/blog")
def create_blog():
    return {"data": "Blog is created"}
