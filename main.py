from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World", "status": "running"}

@app.get("/about")
def about():
    return {"project": "My First API", "author": "Your Name"}
