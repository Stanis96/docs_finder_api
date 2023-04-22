import uvicorn as uvicorn

from fastapi import FastAPI

from .api.base import router_api


app = FastAPI()

app.include_router(router_api)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
