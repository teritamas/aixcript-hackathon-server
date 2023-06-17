from app.facades.database import user_store
from app.master.user.models.domain import User


async def execute(user_id: str) -> User | None:
    user = user_store.fetch_user(user_id)

    return user if user else None
