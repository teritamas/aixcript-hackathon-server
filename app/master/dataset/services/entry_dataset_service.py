import io
from fastapi import BackgroundTasks, UploadFile
from app.facades.chatgpt import create_title
from app.facades.chatgpt.models import CreateChatTitle
from app.facades.database import dataset_store, user_store
from app.facades.storage import image_file_storage
from app.facades.vision_ai import web_detection
from app.facades.vision_ai.models import WebDetectionDto
from app.master.dataset.models.domain import Dataset
from PIL import Image

from app.master.dataset.models.entry_dataset import EntryDatasetRequest
from app.master.user.models.domain import UserDataset
from app.utils.common import generate_id_str


async def execute(
    background_tasks: BackgroundTasks,
    request: EntryDatasetRequest,
    file: UploadFile,
) -> str:
    dataset_id = generate_id_str()

    image_file = await file.read()
    image = Image.open(io.BytesIO(image_file))

    # 拡張子だけ取り除く
    ext = file.filename.split(".")[-1]
    file_name = f"{dataset_id}.{ext}"

    image_file_storage.upload(file_name, image)

    # ChatGPTに生成されたタイトルを入れる
    web_detection_dto: WebDetectionDto = web_detection.execute(image_file)
    create_chat_title: CreateChatTitle = create_title.execute(
        f"概要: {request.description}. AIによって画像から検出されたタグ: {web_detection_dto.best_guess_labels}"
    )

    # firestoreにデータを格納
    content = Dataset.parse_obj(
        {
            **request.dict(),
            **create_chat_title.dict(),
            "dataset_id": dataset_id,
            "file_name": file_name,
        }
    )

    dataset_store.add_dataset(dataset_id, content)

    # ユーザのデータセット一覧に追加
    user_dataset = UserDataset.parse_obj(content.dict())
    user_store.sell_dataset(request.user_id, user_dataset)

    return dataset_id
