from web import app
from flask import url_for
import pytest


@pytest.fixture(scope="module")
def client():
    flask_app = app
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client


def test_index(client):
    response = client.get("/")
    assert b"GREETING" in response.data
    assert response.status_code == 200


def test_url():
    assert url_for("index") == "/"
