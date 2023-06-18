import json
from fastapi.testclient import TestClient
from app.master.dataset.models.entry_dataset import (
    EntryDatasetResponse,
)
from app.main import app
from app.master.dataset.models.purchase_dataset import (
    PurchaseDatasetRequest,
)
from app.facades.web3 import reversible_ft

client = TestClient(app)


def test_entry_dataset_endpoint(mocker):
    # generate_id_strで固定の値を返すmockを作成
    test_dataset_id = "12345"
    mocker.patch(
        "app.master.dataset.services.entry_dataset_service.generate_id_str",
        return_value=test_dataset_id,
    )

    request_payload = {
        "user_id": "sample_user_id",
        "description": "日本の果てで撮影した画像です。",
        "price": 20,
    }

    # Make a request to the endpoint with the sample payload
    response = client.post(
        "/dataset",
        files={
            "request": (
                None,
                json.dumps(request_payload),
            ),
            "file": open("./tests/assets/sample_1.jpeg", "rb"),
        },
    )

    assert response.status_code == 200

    response_data = response.json()
    assert response_data["dataset_id"] is not None

    response_model = EntryDatasetResponse(**response_data)
    assert response_model.dataset_id == response_data["dataset_id"]


def test_list_dataset(mocker):
    test_entry_dataset_endpoint(mocker)

    # Make a request to the endpoint with the sample payload
    response = client.get("/dataset")

    # then
    assert response.status_code == 200
    datasets = response.json()["datasets"]
    assert isinstance(datasets, list)
    assert len(datasets) >= 1


def test_list_dataset_purchased(mocker):
    test_entry_dataset_endpoint(mocker)

    # Make a request to the endpoint with the sample payload
    response = client.get("/dataset?user_id=sample_user_id")

    # then
    assert response.status_code == 200
    datasets = response.json()["datasets"]
    assert isinstance(datasets, list)
    assert len(datasets) >= 1


def test_purchase_dataset(mocker):
    test_entry_dataset_endpoint(mocker)

    # Make a request to the endpoint with the sample payload
    response = client.get("/dataset?user_id=sample_user_id")

    # then
    assert response.status_code == 200
    datasets = response.json()["datasets"]
    assert isinstance(datasets, list)
    assert len(datasets) >= 1


def test_purchase_dataset(mocker):
    test_dataset_id = "12345"
    request = PurchaseDatasetRequest(
        user_id="sample_user_id",
    )

    # テスト用のウォレットアドレスの現在の残高を確認
    sample_user_wallet_address = "0xb872960EF2cBDecFdC64115E1C77067c16f042FB"
    current_deposit = reversible_ft.balance_of_address(sample_user_wallet_address)

    # Send a POST request to the API endpoint
    response = client.post(f"/dataset/{test_dataset_id}/purchased", data=request.json())

    # Assert that the response status code is 200
    assert response.status_code == 200
    assert response.json()["dataset_id"] == test_dataset_id

    # テスト用のウォレットアドレスの残高が減っていることを確認
    now_deposit = reversible_ft.balance_of_address(sample_user_wallet_address)
    assert now_deposit < current_deposit
