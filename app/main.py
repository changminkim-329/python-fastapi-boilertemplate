from fastapi import FastAPI

# hello world

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
