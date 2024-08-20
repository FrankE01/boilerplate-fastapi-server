from core.config import settings

from fastapi import APIRouter

router = APIRouter(prefix=settings.api_prefix, tags=["Config"], include_in_schema=True)

@router.get("/config")
async def get_app_config():
    return {
        "version":settings.version,
        "title":settings.title,
        "api_prefix":settings.api_prefix
        }