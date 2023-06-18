from fastapi import BackgroundTasks
from retry import retry
from app.facades.database import user_store
from app.master.dataset.models.purchase_dataset import PurchaseDatasetRequest
from app.facades.database import dataset_store
from app.master.user.models.domain import UserDataset

from app.facades.web3 import reversible_ft
from app.utils.logging import logger


async def execute(
    dataset_id: str,
    request: PurchaseDatasetRequest,
    background_tasks: BackgroundTasks,
) -> str:
    user = user_store.fetch_user(request.user_id)
    dataset = dataset_store.fetch_dataset(dataset_id)

    # userが存在しない場合はエラー
    if not user or not dataset:
        return "ユーザーまたはデータセットが存在しません"

    try:
        dataset_user = user_store.fetch_user(dataset.user_id)
        # 購入処理
        background_tasks.add_task(
            _brokerage, user.wallet_address, dataset_user.wallet_address, dataset.price
        )
    except Exception as e:
        logger.warn(f"デポジット発行処理で失敗しました.ユーザ登録は完了させます.  {e=}")

    # TODO: 冗長ではあるが両方にデータを入れる
    user_dataset = UserDataset.parse_obj(dataset.dict())
    user_store.purchased_dataset(user.user_id, user_dataset)
    dataset_store.purchased_user(dataset.dataset_id, user)

    return dataset_id


@retry(exceptions=Exception, tries=3)
def _brokerage(
    from_address: str,
    to_address: str,
    amount: int,
):
    reversible_ft.brokerage(
        from_address=from_address, to_address=to_address, amount=amount
    )
