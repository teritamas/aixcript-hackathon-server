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
