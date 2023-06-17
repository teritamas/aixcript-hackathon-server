from typing import List
from app.facades.database import fire_store
from app.master.dataset.models.domain import Dataset
from app.master.user.models.domain import User

COLLECTION_PREFIX = "dataset"


def add_dataset(id: str, content: Dataset):
    """データセットを新規追加する
    Args:
        id (str): datasetId
        content (dataset): 追加するデータセット
    """
    fire_store.add(collection=COLLECTION_PREFIX, id=id, content=content.dict())


def find_datasets() -> List[Dataset]:
    """データセットを全件取得する

    Returns:
        List[Dataset]: データセット一覧
    """
    datasets = fire_store().collection(COLLECTION_PREFIX).stream()
    return [Dataset.parse_obj(dataset.to_dict()) for dataset in datasets]


def fetch_dataset(id: str) -> Dataset:
    """データセットを取得する

    Returns:
        Dataset: データセット
    """
    dataset = fire_store.fetch(collection=COLLECTION_PREFIX, id=id)
    return Dataset.parse_obj(dataset)


def purchased_user(dataset_id: str, user: User):
    """ユーザがデータセットを購入する

    Args:
        dataset (Dataset): 購入するデータセット
    """
    dataset = fetch_dataset(dataset_id)
    dataset.purchased_users.append(user.user_id)

    fire_store.add(collection=COLLECTION_PREFIX, id=dataset_id, content=dataset.dict())
