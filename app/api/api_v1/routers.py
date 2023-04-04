from typing import List

from fastapi import APIRouter
from fastapi import status
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import settings
from app.schemas import Post


router = APIRouter()


client = AsyncIOMotorClient("mongodb://mongo_db:27017/mongo_db")

database = client[settings.MONGO_DB]

post_collection = database.get_collection("posts_collection")


@router.get(
    "/read_all",
    response_description="Retrieved 20 posts",
    response_model=List[Post],
    status_code=status.HTTP_200_OK,
)
async def get_all():
    posts = []
    async for post in post_collection.find().limit(20):
        posts.append(post)
    return posts
