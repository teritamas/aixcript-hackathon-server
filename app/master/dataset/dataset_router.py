from fastapi import APIRouter, BackgroundTasks, Body, File, UploadFile

from app.master.dataset.models.entry_dataset import (
    EntryDatasetRequest,
    EntryDatasetResponse,
)
from app.master.dataset.models.list_dataset import ListDatasetResponse
from app.master.dataset.models.purchase_dataset import (
    PurchaseDatasetRequest,
    PurchasedDatasetResponse,
)

from app.master.dataset.services import (
    entry_dataset_service,
    list_dataset_service,
    purchase_dataset_service,
)


dataset_router = APIRouter(prefix="/dataset", tags=["dataset"])


@dataset_router.post(
    "", description="データセット登録API.", response_model=EntryDatasetResponse
)
async def entry_dataset(
    background_tasks: BackgroundTasks,
    request: EntryDatasetRequest = Body(...),
    file: UploadFile = File(...),
):
    dataset_id = await entry_dataset_service.execute(
        background_tasks=background_tasks,
        request=request,
        file=file,
    )
    return EntryDatasetResponse(dataset_id=dataset_id)


@dataset_router.get(
    "", description="データセット一覧取得API.", response_model=ListDatasetResponse
)
async def list_dataset():
    datasets = await list_dataset_service.execute()
    return ListDatasetResponse(datasets=datasets)


@dataset_router.post(
    "/{dataset_id}/purchased",
    description="データセット購入API.",
    response_model=PurchasedDatasetResponse,
)
async def purchase_dataset(
    dataset_id: str,
    request: PurchaseDatasetRequest,
):
    dataset_id = await purchase_dataset_service.execute(
        dataset_id=dataset_id,
        request=request,
    )
    return PurchasedDatasetResponse(dataset_id=dataset_id)
