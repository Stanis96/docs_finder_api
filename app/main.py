import uvicorn as uvicorn

from fastapi import FastAPI

from .api.api_v1.routers import router


app = FastAPI()


# @app.on_event("startup")
# async def startup_db():
#     app.db_client = AsyncIOMotorClient(settings.MONGODB_URL)
#     app.mongodb = app.db_client[settings.DB_NAME]
#     app.include_router(router)
#
#
# @app.on_event("shutdown")
# async def shutdown_db():
#     app.db_client.close()


app.include_router(router, tags=["posts"], prefix="/post")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
