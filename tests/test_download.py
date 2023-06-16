from fastapi.testclient import TestClient

from app.main import app
from app.master.user.models.domain import User

client = TestClient(app)


def test_download_file():
    # give
    test_wallet_address = "0xb872960EF2cBDecFdC64115E1C77067c16f042FB"

    response = client.get(
        f"/download/{test_wallet_address}",
    )

    assert response.status_code == 200
