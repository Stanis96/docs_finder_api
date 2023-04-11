from typing import Any
from typing import List

from fastapi import APIRouter
from fastapi import status
from motor.motor_asyncio import AsyncIOMotorClient

from app.schemas import Post


router = APIRouter()


client: AsyncIOMotorClient = AsyncIOMotorClient("mongodb://mongo_db:27017/mongo_db")
# client: AsyncIOMotorClient = AsyncIOMotorClient("mongodb://user:pass@mongo_db:27017/mongo_db")
database = client.get_database("mongo_db")

post_collection = database.get_collection("posts_collection")


async def search_data(key_word: str, search_item: str) -> List:
    list_data = []
    query = {f"{key_word}": {"$regex": f"{search_item}"}}
    async for post in post_collection.find(query):
        list_data.append(post)
    return list_data


@router.get(
    "/read_20",
    response_description="Retrieved 20 test posts",
    response_model=List[Post],
    status_code=status.HTTP_200_OK,
)
async def get_test():
    posts = []
    async for post in post_collection.find().limit(20):
        posts.append(post)
    return posts


@router.get(
    "/search_text",
    response_description="Search for posts in text",
    response_model=List[Post],
    status_code=status.HTTP_200_OK,
)
async def search_text_post(word: str) -> Any:
    return await search_data(key_word="text", search_item=word)


@router.get(
    "/search_date",
    response_description="Search posts by date",
    response_model=List[Post],
    status_code=status.HTTP_200_OK,
)
async def search_post_by_date(date: str) -> Any:
    return await search_data(key_word="created_date", search_item=date)
