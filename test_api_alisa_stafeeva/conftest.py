import pytest
from endpoints.create_object import CreateObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject


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
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def object_id(create_object_endpoint, delete_object_endpoint):
    body = {"name": "alisa_object_2", "data": {"color": "black", "size": "giant"}}
    create_object_endpoint.new_object(body)
    yield create_object_endpoint.object_id
    delete_object_endpoint.delete_an_object(object_id)
