from typing import List
from pydantic import BaseModel, Field


class CreateChatTitle(BaseModel):
    title: str = Field("", description="タイトル")
    tags: List[str] = Field([], description="タグ")
