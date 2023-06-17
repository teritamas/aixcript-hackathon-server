from enum import Enum
from typing import List
from pydantic import BaseModel, Field

from app.master.dataset.models.domain import Dataset


class DatasetOwnType(str, Enum):
    UNKNOWN = "unknown"  # ユーザIDを取得できないため不明
    PURCHASED = "purchased"  # 自身の提案でなく購入済みのもの
    UN_PURCHASED = "un_purchased"  # 自身の提案でなく購入済みでないもの
    OWNER = "owner"  # 所有者


class ListDatasetDto(Dataset):
    dataset_own_type: DatasetOwnType = Field(
        DatasetOwnType.UNKNOWN, description="データセットの所有者"
    )


class ListDatasetResponse(BaseModel):
    datasets: List[ListDatasetDto] = Field([], description="データセット一覧")
