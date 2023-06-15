from typing import List
from pydantic import BaseModel, Field

from app.master.dataset.models.domain import Dataset


class ListDatasetResponse(BaseModel):
    datasets: List[Dataset] = Field([], description="データセット一覧")
