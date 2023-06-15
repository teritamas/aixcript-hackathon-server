from typing import List
from app.facades.database import fire_store
from app.master.dataset.models.domain import Dataset

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
