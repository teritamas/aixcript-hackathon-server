from typing import List
from pydantic import BaseModel, Field


class UserDataset(BaseModel):
    dataset_id: str = Field("", description="データセットID")
    user_id: str = Field("", description="作成者のユーザID")

    title: str = Field("", description="データセットのタイトル")
    description: str = Field("", description="データセットの詳細")

    file_name: str = Field("", description="ファイル名")

    price: int = Field(0, description="価格")
    tags: list = Field([], description="タグ")


class User(BaseModel):
    # id
    user_id: str = Field("", description="ユーザID")
    user_name: str = Field("", description="ユーザ名")
    # ウォレットアドレス
    wallet_address: str = Field("", description="ウォレットアドレス")

    # 保有トークン量
    deposit: int = Field(-1, description="保有トークン量(-1の時は取得失敗)")

    # 購入したデータセット一覧
    purchase_datasets: List[UserDataset] = Field([], description="購入したデータセット一覧")
    # 販売したデータセット一覧
    sell_datasets: List[UserDataset] = Field([], description="販売したデータセット一覧")
