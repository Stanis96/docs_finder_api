import os
import sys

from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings
from pydantic import MongoDsn


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(BASE_DIR)


class Settings(BaseSettings):
    PROJECT_TITLE: Optional[str]
    PROJECT_VERSION: Optional[str]
    PROJECT_DESCRIPTION: Optional[str]

    MONGO_URI: Optional[MongoDsn]
    MONGO_DB: str
    MONGO_COLLECTION: Optional[str]

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings(_env_file=".env")  # type: ignore
