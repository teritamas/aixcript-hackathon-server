import os
from fastapi import (
    APIRouter,
    BackgroundTasks,
    Body,
    File,
    HTTPException,
    UploadFile,
    status,
)

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
    download_dataset_thumbnail_service,
)
from fastapi.responses import FileResponse

dataset_router = APIRouter(prefix="/dataset", tags=["dataset"])


def remove_file(path: str) -> None:
    os.unlink(path)


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


@dataset_router.get(
    "/{dataset_id}/thumbnail",
    description="サムネイル取得API",
    response_class=FileResponse,
    response_description="データセットのサムネイル",
)
def download_proposal_thumbnail(
    dataset_id: str,
    background_tasks: BackgroundTasks,
):
    response = download_dataset_thumbnail_service.execute(dataset_id=dataset_id)
    if response:
        background_tasks.add_task(remove_file, response)  # 実行後ファイルを削除
        return FileResponse(
            path=response,
            media_type="image/jpeg",
        )
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


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
