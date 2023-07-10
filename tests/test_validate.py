from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_validate_endpoint():
    # send a POST request to the /validate endpoint
    response = client.post(
        "/validate", files={"file": open("./tests/assets/sample_1.jpeg", "rb")}
    )

    # assert that the response has a 200 status code
    assert response.status_code == 200

    # assert that the response contains the expected keys in the JSON body
    response_json = response.json()
    assert 5 == len(response_json["full_math_url"])
    assert 5 == len(response_json["partial_math_urls"])
    assert 5 == len(response_json["similar_urls"])
    assert 2 == len(response_json["tags"])
    assert not response_json["is_registerable"]
