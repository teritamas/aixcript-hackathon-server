import os
from fastapi import (
    APIRouter,
    BackgroundTasks,
    HTTPException,
    Response,
    status,
)


from app.master.download.services import (
    download_service,
)
from fastapi.responses import FileResponse

download_router = APIRouter(prefix="/download", tags=["download"])


def remove_file(path: str) -> None:
    os.unlink(path)


@download_router.get(
    "/{wallet_address}",
    description="画像取得API",
    response_class=FileResponse,
    response_description="提案のサムネイル",
)
async def download(
    wallet_address: str,
    background_tasks: BackgroundTasks,
):
    zipfile_name = await download_service.execute(wallet_address=wallet_address)
    if zipfile_name:
        background_tasks.add_task(remove_file, zipfile_name)  # 実行後ファイルを削除

        # zipファイルを返す
        response = Response(
            content=open(zipfile_name, "rb").read(),
            media_type="application/x-zip-compressed",
        )

        # ファイルの送信
        response.headers["Content-Disposition"] = f"attachment; filename={zipfile_name}"

        return response
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
