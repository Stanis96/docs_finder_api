from typing import Optional

from pydantic import BaseModel


class PostBase(BaseModel):
    id: str
    text: str
    created_date: Optional[str]
    rubrics: Optional[str]


class Post(BaseModel):
    text: str
    created_date: Optional[str]
    rubrics: Optional[str]
