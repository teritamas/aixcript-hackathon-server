from pydantic import BaseModel, Field


class EntryUserRequest(BaseModel):
    user_name: str = Field("", description="ユーザ名")
    wallet_address: str = Field("", description="ユーザ名")


class EntryUserResponse(BaseModel):
    user_id: str = Field("", description="ユーザID")
