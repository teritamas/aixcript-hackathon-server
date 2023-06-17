from app.facades.database import user_store
from app.master.dataset.models.purchase_dataset import PurchaseDatasetRequest
from app.facades.database import dataset_store
from app.master.user.models.domain import UserDataset


async def execute(
    dataset_id: str,
    request: PurchaseDatasetRequest,
) -> str:
    user = user_store.fetch_user(request.user_id)
    dataset = dataset_store.fetch_dataset(dataset_id)
    # userが存在しない場合はエラー
    if not user or not dataset:
        return "ユーザーまたはデータセットが存在しません"

    # TODO: 冗長ではあるが両方にデータを入れる
    user_dataset = UserDataset.parse_obj(dataset.dict())
    user_store.purchased_dataset(user.user_id, user_dataset)
    dataset_store.purchased_user(dataset.dataset_id, user)

    return dataset_id
