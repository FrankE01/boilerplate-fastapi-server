from fastapi import APIRouter

from api.v1.routers import configurations

app_router = APIRouter()

app_router.include_router(configurations.router)