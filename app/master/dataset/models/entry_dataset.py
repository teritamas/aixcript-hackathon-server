import json
from pydantic import BaseModel, Field


class EntryDatasetResponse(BaseModel):
    dataset_id: str = Field("", description="データセットID")


class EntryDatasetRequest(BaseModel):
    user_id: str = Field("", description="ユーザID")
    description: str = Field("", description="データセットの詳細")

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value
