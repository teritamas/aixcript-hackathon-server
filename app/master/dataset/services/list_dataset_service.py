from app.facades.database import dataset_store, user_store
from app.master.dataset.models.list_dataset import DatasetOwnType, ListDatasetDto


async def execute(
    user_id: str | None = None,
):
    # FireStoreからDatasetの一覧を取得
    datasets = dataset_store.find_datasets()

    responses = []
    for dataset in datasets:
        list_dataset_dto = ListDatasetDto.parse_obj(dataset.dict())
        if user_id is None:
            list_dataset_dto.dataset_own_type = DatasetOwnType.UNKNOWN
        elif user_id == dataset.user_id:
            list_dataset_dto.dataset_own_type = DatasetOwnType.OWNER
        elif _user_purchased(dataset_id=dataset.dataset_id, user_id=user_id):
            list_dataset_dto.dataset_own_type = DatasetOwnType.PURCHASED
        else:
            list_dataset_dto.dataset_own_type = DatasetOwnType.UN_PURCHASED

        responses.append(list_dataset_dto)
    return responses


def _user_purchased(dataset_id: str, user_id: str):
    """ユーザが投票済みの場合Trueを返す"""
    user = user_store.fetch_user(user_id)
    own_dataset = [
        dataset
        for dataset in user.purchase_datasets
        if dataset.dataset_id == dataset_id
    ]
    if own_dataset != []:  # 購入済み場合アクセス可能
        return True
    else:
        return False
