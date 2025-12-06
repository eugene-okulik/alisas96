import pytest
import requests


@pytest.fixture(scope="session")
def start_end():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture()
def before_after():
    print("before test")
    yield
    print("after test")


@pytest.fixture()
def new_object():
    body = {"name": "alisa_object_2", "data": {"color": "black", "size": "giant"}}
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        "http://objapi.course.qa-practice.com/object", json=body, headers=headers
    )
    object_id = response.json()["id"]
    yield object_id
    requests.delete(f"http://objapi.course.qa-practice.com/object/{object_id}")
