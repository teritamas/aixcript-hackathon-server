from fastapi import (
    APIRouter,
    BackgroundTasks,
    HTTPException,
    status,
)


from app.master.user.models.detail_user import DetailUserResponse

from app.master.user.models.entry_user import EntryUserRequest, EntryUserResponse
from app.master.user.services import (
    entry_user_service,
    fetch_user_service,
    detail_user_by_wallet_address_service,
)

user_router = APIRouter(prefix="", tags=["user"])


@user_router.post("/signup", description="サインアップ.", response_model=EntryUserResponse)
async def signup(request: EntryUserRequest, background_tasks: BackgroundTasks):
    user_id = await entry_user_service.execute(
        request=request, background_tasks=background_tasks
    )
    return EntryUserResponse(user_id=user_id)


@user_router.get(
    "/user/{user_id}",
    description="ユーザ詳細情報取得",
    response_model=DetailUserResponse,
)
async def fetch_user(user_id: str):
    user = await fetch_user_service.execute(user_id)
    if user:
        return DetailUserResponse(**user.dict())
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@user_router.get(
    "/login/wallet_address/{wallet_address}",
    description="ウォレットアドレスからユーザ情報を取得.",
    response_model=DetailUserResponse,
)
async def login_wallet_address(
    wallet_address: str,
):
    user = await detail_user_by_wallet_address_service.execute(wallet_address)
    if user:
        return DetailUserResponse(**user.dict())
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
