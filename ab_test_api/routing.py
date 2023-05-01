from fastapi import Header
from fastapi import APIRouter


router = APIRouter()


@router.get("/api/v1/get-test/")
async def tests(device_token=Header(None, alias='Device-Token')):
    if device_token == '123':
        return {"message": "Something else"}
    return {"message": "Hello World"}


@router.get("/")
async def root():
    return {"message": "Done!"}
