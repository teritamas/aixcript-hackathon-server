from fastapi import APIRouter, File, UploadFile
from app.master.validate.models.domain import ValidateResult

from app.master.validate.models.validate_request import ValidateResponse
from app.master.validate.services import validate_service

validate_router = APIRouter(prefix="/validate", tags=["validate"])


@validate_router.post("", description="画像の検証用API", response_model=ValidateResponse)
async def validate(
    file: UploadFile = File(...),
):
    response: ValidateResult = await validate_service.execute(file)
    return ValidateResponse(**response.dict())
