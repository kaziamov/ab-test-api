from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/get-test/")
async def root():
    return {"message": "Hello World"}