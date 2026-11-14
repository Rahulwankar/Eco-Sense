from fastapi import FastAPI
from src.config.database import Base, engine
from src.config.cors import setup_cors

Base.metadata.create_all(engine)

app = FastAPI()

setup_cors(app)

@app.get("/db-connection")
def home():
    return {
        "message": "FastAPI is running successfully"
    }