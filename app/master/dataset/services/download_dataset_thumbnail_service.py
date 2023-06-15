import os

from app.facades.database import dataset_store
from app.facades.storage import image_file_storage


def execute(dataset_id: str) -> str:
    dataset = dataset_store.fetch_dataset(dataset_id)

    if not dataset:
        return "データセットが存在しません"

    download_byte = image_file_storage.download(dataset.file_name)

    with open(os.path.basename(dataset.file_name), "wb") as f:
        f.write(download_byte)

    return dataset.file_name
