from fastapi import FastAPI

from ab_test_api.routing import router

app = FastAPI()
app.include_router(router=router)
