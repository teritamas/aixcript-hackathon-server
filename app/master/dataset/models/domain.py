from typing import List
from pydantic import BaseModel, Field

from datetime import datetime

from app.utils.common import now


class Dataset(BaseModel):
    dataset_id: str = Field("", description="データセットID")
    user_id: str = Field("", description="所有者のユーザID")

    title: str = Field("", description="データセットのタイトル(自動生成される)")
    description: str = Field("", description="データセットの詳細")

    file_name: str = Field("", description="ファイル名")

    price: int = Field(0, description="価格")
    tags: list = Field([], description="タグ")

    purchased_users: List[str] = Field([], description="購入したユーザ一覧")

    created_at: datetime = Field(now(), description="作成時刻")
    updated_at: datetime = Field(now(), description="編集時刻")
