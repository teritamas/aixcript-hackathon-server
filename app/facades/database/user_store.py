from app.facades.database import fire_store
from app.master.dataset.models.domain import Dataset
from app.master.user.models.domain import User


COLLECTION_PREFIX = "users"


def add_user(id: str, content: User):
    """ユーザを新規追加する

    Args:
        id (str): UserId
        content (User): 追加するユーザ情報
    """
    fire_store.add(collection=COLLECTION_PREFIX, id=id, content=content.dict())


def fetch_user(id: str) -> User | None:
    """idからユーザ情報を検索する。

    Args:
        id (str): ユーザ情報

    Returns:
        User | None:
    """
    user_dict = fire_store.fetch(collection=COLLECTION_PREFIX, id=id)
    return User.parse_obj(user_dict) if user_dict else None


def purchased_dataset(user_id: str, dataset: Dataset):
    """ユーザがデータセットを購入する

    Args:
        dataset (Dataset): 購入するデータセット
    """
    user = fetch_user(user_id)
    user.purchase_datasets.append(dataset)

    fire_store.add(collection=COLLECTION_PREFIX, id=user_id, content=user.dict())
