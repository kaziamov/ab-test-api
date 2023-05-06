from fastapi import Header
from fastapi import APIRouter

from ab_test_api.crud import get_device, add_device, test_select
# from ab_test_api.db_connect import conn_pool

router = APIRouter()


@router.get("/api/v1/get-test/")
async def tests(device_token=Header(None, alias='Device-Token')):
    device = test_select(device_token)
    return {"device_token": device_token, "message": device }


@router.get("/")
async def root():
    return {"message": "Done!"}
