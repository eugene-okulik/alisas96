import requests
import pytest


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


@pytest.mark.critical
@pytest.mark.parametrize(
    "body_value",
    [
        {"name": "alisa_object_11", "data": {"color": "red", "size": "big"}},
        {"name": "alisa_object_22", "data": {"color": "cian", "size": "small"}},
        {"name": "alisa_object_33", "data": {"color": "white", "size": "medium"}},
    ],
)
def test_post_an_object(start_end, before_after, body_value):
    body = body_value
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        "http://objapi.course.qa-practice.com/object", json=body, headers=headers
    )
    assert response.status_code == 200, "Status is incorrect"
    assert response.json()["name"] == body["name"], "Name is incorrect"


@pytest.mark.medium
def test_put_an_object(before_after, new_object):
    body = {"name": "alisa_object_2", "data": {"color": "red", "size": "big"}}
    headers = {"Content-Type": "application/json"}
    response = requests.put(
        f"http://objapi.course.qa-practice.com/object/{new_object}",
        json=body,
        headers=headers,
    )
    assert response.status_code == 200, "Put failed"
    assert response.json()["data"] == {"color": "red", "size": "big"}


def test_patch_an_object(before_after, new_object):
    body = {"data": {"color": "red", "size": "big"}}
    headers = {"Content-Type": "application/json"}
    response = requests.patch(
        f"http://objapi.course.qa-practice.com/object/{new_object}",
        json=body,
        headers=headers,
    )
    assert response.status_code == 200, "Patch failed"
    assert response.json()["data"] == {"color": "red", "size": "big"}


def test_delete_an_object(before_after, new_object):

    response = requests.delete(
        f"http://objapi.course.qa-practice.com/object/{new_object}"
    )
    assert response.status_code == 200, "Delete failed"
