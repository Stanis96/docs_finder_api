import asyncio
import json
import os

import pandas as pd

from motor.motor_asyncio import AsyncIOMotorClient

from .config import settings


async def import_data():
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    db = client[settings.DB_NAME]
    collection = db[settings.DB_COLLECTION]
    cdir = os.path.dirname(__file__)
    filepath = "static/posts.csv"
    file_res = os.path.join(cdir, filepath)
    try:
        data = pd.read_csv(file_res, header=None)
    except FileNotFoundError:
        print(f"File {filepath} not found.")
        return
    except pd.errors.EmptyDataError:
        print(f"File {filepath} is empty.")
        return
    data_json = json.loads(data.to_json(orient="records"))
    await collection.insert_many(data_json)


if __name__ == "__main__":
    asyncio.run(import_data())
