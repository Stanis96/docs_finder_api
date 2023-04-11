from fastapi import APIRouter

from .api_v1 import routers


router_api = APIRouter()
router_api.include_router(routers.router, tags=["posts"], prefix="/api/v1/post")
