import os
import sys

from dotenv import load_dotenv
from pydantic import BaseSettings


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(BASE_DIR)


class Settings(BaseSettings):
    MONGO_URL: str
    MONGO_DB: str
    MONGO_COLLECTION: str

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings(_env_file=".env")  # type: ignore
