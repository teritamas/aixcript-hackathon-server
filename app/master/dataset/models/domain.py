from pydantic import BaseModel, Field

from datetime import datetime

from app.utils.common import now


class Dataset(BaseModel):
    user_id: str = Field("", description="所有者のユーザID")
    description: str = Field("", description="データセットの詳細")

    created_at: datetime = Field(now(), description="作成時刻")
    updated_at: datetime = Field(now(), description="編集時刻")
