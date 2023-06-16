from app.facades.database import user_store
from app.master.user.models.domain import User


async def execute(wallet_address: str) -> User | None:
    users = user_store.fetch_user_from_wallet_address(wallet_address)

    return users[0] if len(users) != 0 else None
