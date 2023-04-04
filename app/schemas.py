from typing import Optional

from pydantic import BaseModel


class PostBase(BaseModel):
    text: Optional[str]
    created_date: Optional[str]
    rubrics: Optional[str]


class Post(PostBase):
    _id: Optional[str]
