from typing import List

from fastapi import APIRouter
from fastapi import Request
from fastapi import status

from app.config import settings
from app.schemas import Post


router = APIRouter()


@router.get(
    "/show/",
    response_description="Get 20 matching posts",
    response_model=List[Post],
    status_code=status.HTTP_200_OK,
)
async def search_posts(search_terms: str, request: Request):
    db = request.app.mongodb
    collection = db[settings.DB_COLLECTION]
    query = {"$text": {"$search": search_terms}}
    result = await collection.find(query).limit(20).to_list(length=20)
    return result
