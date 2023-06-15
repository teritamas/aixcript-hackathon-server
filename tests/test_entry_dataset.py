import json
from fastapi.testclient import TestClient
from app.master.dataset.models.entry_dataset import (
    EntryDatasetResponse,
)
from app.main import app

client = TestClient(app)


def test_entry_dataset_endpoint():
    request_payload = {"user_id": "sample data", "description": "sample name"}
    # ダミーのzipファイルを作成

    # Make a request to the endpoint with the sample payload
    response = client.post(
        "/dataset",
        files={
            "request": (
                None,
                json.dumps(request_payload),
            ),
            "file": open("./tests/assets/sample_1.zip", "rb"),
        },
    )

    assert response.status_code == 200

    response_data = response.json()
    assert response_data["dataset_id"] is not None

    response_model = EntryDatasetResponse(**response_data)
    assert response_model.dataset_id == response_data["dataset_id"]


def test_list_dataset():
    test_entry_dataset_endpoint()
    response = client.get("/dataset")
    assert response.status_code == 200
    datasets = response.json()["datasets"]
    assert isinstance(datasets, list)
    assert len(datasets) >= 1
