from typing import List
from pydantic import BaseModel, Field


from app.master.dataset.models.domain import Dataset


class User(BaseModel):
    # id
    user_id: str = Field("", description="ユーザID")
    user_name: str = Field("", description="ユーザ名")
    # ウォレットアドレス
    wallet_address: str = Field("", description="ウォレットアドレス")

    # 購入したデータセット一覧
    purchase_datasets: List[Dataset] = Field([], description="購入したデータセット一覧")
