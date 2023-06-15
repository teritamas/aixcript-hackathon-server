from pydantic import BaseModel, Field


class PurchaseDatasetRequest(BaseModel):
    user_id: str = Field(..., description="購入するユーザのユーザID")


class PurchasedDatasetResponse(BaseModel):
    dataset_id: str = Field(..., description="データセットID")
