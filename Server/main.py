from fastapi import FastAPI
from src.config.database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/db-connection")
def home():
    return {
        "message": "FastAPI is running successfully"
    }