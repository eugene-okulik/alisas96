import pytest
import requests
from endpoints.create_object import CreateObject
from endpoints.update_object import UpdateObject


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
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def object_id(create_object_endpoint):
    body = {"name": "alisa_object_2", "data": {"color": "black", "size": "giant"}}
    create_object_endpoint.new_object(body)
    yield create_object_endpoint.object_id
    requests.delete(f"http://objapi.course.qa-practice.com/object/{object_id}")
