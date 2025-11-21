from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World", "status": "running"}

@app.get("/about")
def about():
    return {"project": "My First API", "author": "Aayush Raj"}

@app.get("/items")
def items():
    return {"laptop": "ColorFul","gpu": "RTX 4060"}
