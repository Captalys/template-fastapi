from pytest import fixture
from fastapi.testclient import TestClient

from src.app import app


@fixture
def client():
    client = TestClient(app)
    yield client


@fixture
def user():
    return dict(
        name="TestUser",
        email="test.user@testemail.com"
    )
