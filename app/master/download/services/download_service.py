import os
from zipfile import ZIP_DEFLATED, ZipFile
from app.facades.database import user_store
from app.facades.storage import image_file_storage
from app.master.user.models.domain import User
from app.utils.common import generate_id_str
from app.utils.logging import logger

TEMP_FOLDER_NAME = "./app/temp/zip"


async def execute(
    wallet_address: str,
):
    """wallet_addressに紐づくユーザが購入した画像の一覧を取得し、zipファイルを作成して返す

    Args:
        wallet_address (str): _description_
    """
    user: User = user_store.fetch_user_from_wallet_address(wallet_address)

    if not user:
        logger.error(f"User not found. wallet_address: {wallet_address}")
        return None

    uuid = generate_id_str()
    zipfile_name = f"{uuid}.zip"
    temp_file_path = f"{TEMP_FOLDER_NAME}/{uuid}"

    # ダウンロードしてzipファイルを作成
    with ZipFile(
        zipfile_name, "w", compression=ZIP_DEFLATED, compresslevel=9
    ) as new_zip:
        os.makedirs(temp_file_path, exist_ok=True)
        for dataset in user.purchase_datasets:
            image_temp_path = download_image(temp_file_path, dataset.file_name)
            new_zip.write(image_temp_path, arcname=dataset.file_name)
        new_zip.close()

    return zipfile_name


def download_image(temp_file_path, file_name):
    """画像をダウンロードして一時的に保存する

    Args:
        temp_file_path (_type_): _description_
        dataset (_type_): _description_

    Returns:
        _type_: _description_
    """
    file = image_file_storage.download(file_name)
    image_temp_path = f"{temp_file_path}/{file_name}"
    with open(image_temp_path, "wb") as f:
        f.write(file)
    return image_temp_path
