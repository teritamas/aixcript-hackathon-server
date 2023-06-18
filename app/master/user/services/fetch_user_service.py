import re
from app.facades.database import user_store
from app.master.user.models.domain import User
from app.facades.web3 import reversible_ft


async def execute(user_id: str) -> User | None:
    user = user_store.fetch_user(user_id)

    # ユーザが存在しない場合はNoneを返す
    if user is None:
        return None

    # ユーザが存在する場合トークン量を取得し返す。
    wallet_address = user.wallet_address
    if wallet_address is None:
        return user

    user.deposit = reversible_ft.balance_of_address(user.wallet_address)
    return user
