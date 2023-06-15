from app.facades.database import user_store
from app.master.dataset.models.purchase_dataset import PurchaseDatasetRequest
from app.facades.database import dataset_store


async def execute(
    dataset_id: str,
    request: PurchaseDatasetRequest,
) -> str:
    user = user_store.fetch_user(request.user_id)
    dataset = dataset_store.fetch_dataset(dataset_id)
    # userが存在しない場合はエラー
    if not user or not dataset:
        return "ユーザーまたはデータセットが存在しません"

    user_store.purchased_dataset(user.user_id, dataset)

    return dataset_id
