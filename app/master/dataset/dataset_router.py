from fastapi import APIRouter, BackgroundTasks, Body, File, UploadFile

from app.master.dataset.models.entry_dataset import (
    EntryDatasetRequest,
    EntryDatasetResponse,
)

from app.master.dataset.services import entry_dataset_service


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


# @dataset_router.get(
#     "", description="データセット一覧取得API.", response_model=ListDatasetResponse
# )
# async def entry_dataset(
#     background_tasks: BackgroundTasks,
#     request: EntryDatasetRequest = Body(...),
#     file: UploadFile = File(...),
# ):
#     dataset_id = await entry_dataset_service.execute(
#         background_tasks=background_tasks,
#         request=request,
#         file=file,
#     )
#     return EntryDatasetResponse(dataset_id=dataset_id)
