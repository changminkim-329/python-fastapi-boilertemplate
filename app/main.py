from fastapi import FastAPI
from models.base import *

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}
