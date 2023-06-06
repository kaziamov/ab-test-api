from fastapi import Header
from fastapi import APIRouter

from ab_test_api.logic import get_or_create_test

router = APIRouter()


@router.get("/api/v1/get-test/")
async def tests(device_token=Header(None, alias='Device-Token')) -> dict:
    result = await get_or_create_test(device_token)
    return {"device_token": device_token, "message": result}
