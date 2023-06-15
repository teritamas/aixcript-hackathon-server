from app.facades.storage import gcs
from app.utils.logging import logger

import os

FOLDER_NAME = "ZipFile"


def upload(
    destination_blob_name: str,
    zip_file: bytes,
) -> str:
    # zip_fileをローカルに保存
    with open(f"{destination_blob_name}.zip", "wb") as f:
        f.write(zip_file)

    try:
        blob = gcs().blob(f"{FOLDER_NAME}/{destination_blob_name}.zip")

        # Upload the file to GCS
        blob.upload_from_filename(f"{destination_blob_name}.zip")
        logger.info(f"File uploaded to {destination_blob_name}.")
    except Exception as e:
        logger.error(f"upload error. {e}")
    finally:
        # ローカルのzipファイルを削除
        os.remove(f"{destination_blob_name}.zip")


def download(destination_blob_name: str) -> bytes:
    blob = gcs().blob(f"{FOLDER_NAME}/{destination_blob_name}")

    return blob.download_as_bytes()


def delete(destination_blob_name: str):
    blob = gcs().blob(f"{FOLDER_NAME}/{destination_blob_name}")
    if blob.exists():
        blob.delete()
