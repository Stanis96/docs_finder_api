from typing import Any
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from motor.motor_asyncio import AsyncIOMotorClient

from app.schemas import Post
from app.schemas import PostBase


router = APIRouter()


async def get_prod_client() -> AsyncIOMotorClient:
    client: AsyncIOMotorClient = AsyncIOMotorClient("mongodb://mongo_db:27017/")
    return client


async def search_data(
    key_word: str, search_item: str, client: AsyncIOMotorClient = Depends(get_prod_client)
) -> Any:
    query = {f"{key_word}": {"$regex": f"{search_item}"}}
    database = client.get_database("mongo_db")
    post_collection = database.get_collection("posts_collection")
    post = await post_collection.find(query).to_list(None)

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{search_item} not found!"
        )
    return post


@router.get(
    "/retrieve_all",
    response_description="Retrieve all data",
    response_model=List[PostBase],
    status_code=status.HTTP_200_OK,
)
async def get_all(client: AsyncIOMotorClient = Depends(get_prod_client)) -> Any:
    database = client.get_database("mongo_db")
    post_collection = database.get_collection("posts_collection")
    posts = await post_collection.find().to_list(None)
    return posts


@router.get(
    "/search_current_page",
    response_description="Set the number of entries and page number",
    response_model=List[Post],
    status_code=status.HTTP_200_OK,
)
async def search_page(
    page_size: int, page_num: int, client: AsyncIOMotorClient = Depends(get_prod_client)
) -> Any:
    skips = page_size * (page_num - 1)
    database = client.get_database("mongo_db")
    post_collection = database.get_collection("posts_collection")
    posts = await post_collection.find().skip(skips).limit(page_size).to_list(None)
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Values not found!")
    return posts


@router.get(
    "/search_text",
    response_description="Search for posts in text",
    response_model=List[Post],
    status_code=status.HTTP_200_OK,
)
async def search_text_post(word: str, client: AsyncIOMotorClient = Depends(get_prod_client)) -> Any:
    return await search_data(key_word="text", search_item=word, client=client)


@router.get(
    "/search_date",
    response_description="Search posts by date",
    response_model=List[Post],
    status_code=status.HTTP_200_OK,
)
async def search_post_by_date(
    date: str, client: AsyncIOMotorClient = Depends(get_prod_client)
) -> Any:
    return await search_data(key_word="created_date", search_item=date, client=client)
