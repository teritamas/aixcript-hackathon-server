from fastapi import BackgroundTasks, UploadFile
from app.facades.database import dataset_store
from app.facades.storage import zipfile_storage
from app.master.dataset.models.domain import Dataset

from app.master.dataset.models.entry_dataset import EntryDatasetRequest
from app.utils.common import generate_id_str


async def execute(
    background_tasks: BackgroundTasks,
    request: EntryDatasetRequest,
    file: UploadFile,
) -> str:
    dataset_id = generate_id_str()

    # fileがzipかどうかを判定
    if not file.filename.endswith(".zip"):
        return "zipファイルをアップロードしてください"

    # zipを変数に格納
    zip_file = await file.read()
    zipfile_storage.upload(dataset_id, zip_file)

    # firestoreにデータを格納
    content = Dataset.parse_obj({**request.dict(), dataset_id: dataset_id})

    dataset_store.add_dataset(dataset_id, content)

    return dataset_id
