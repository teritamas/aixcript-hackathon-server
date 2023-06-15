from app.facades.database import dataset_store


async def execute():
    # FireStoreからDatasetの一覧を取得
    datasets = dataset_store.find_datasets()
    return datasets
