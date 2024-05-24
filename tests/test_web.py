from web import app, Todo
from flask import url_for
import pytest


@pytest.fixture
def client():
    flask_app = app
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client


def test_index(client):
    response = client.get("/")
    assert b"GREETING" in response.data
    assert response.status_code == 200


def test_todo_model():
    # Create a Todo instance for testing
    todo = Todo(title="Test Title", message="Test Message")

    # Assert that the title and message match the values set above
    assert todo.title == "Test Title"
    assert todo.message == "Test Message"


def test_url():
    with app.test_request_context():
        assert url_for("index") == "/"
