from mongomock_motor import AsyncMongoMockClient
from fastapi.testclient import TestClient

from app.api.api_v1.routers import get_prod_client
from app.main import app


test_client = AsyncMongoMockClient()


async def get_test_client():
    return test_client


app.dependency_overrides[get_prod_client] = get_test_client


async def test_retrieve_all():
    db = test_client.get_database("mongo_db")
    collection = db.get_collection("post_collection")
    data = [
        {"_id": "1", "text": "test", "created_date": "2022-06-27", "rubrics": "test case"},
        {"_id": "2", "text": "test2", "created_date": "2022-06-26", "rubrics": "test case2"},
    ]
    await collection.insert_many(data)
    assert len(await collection.find({}).to_list(None)) == 2
    client = TestClient(app)
    response = client.get("/api/v1/post/retrieve_all")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(isinstance(post, dict) for post in response.json())
    collection.delete_many({})


async def test_conn():
    client = TestClient(app)
    response = client.get("/docs")
    assert response.status_code == 200
