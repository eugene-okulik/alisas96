import requests
import pytest
import allure


@allure.feature('New object')
@allure.story('Create an object')
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


@allure.feature('Existing object')
@allure.story('Put an object')
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


@allure.feature('Existing object')
@allure.story('Patch an object')
def test_patch_an_object(before_after, new_object):
    with allure.step('Prepare test data'):
        body = {"data": {"color": "red", "size": "big"}}
        headers = {"Content-Type": "application/json"}
        response = requests.patch(
            f"http://objapi.course.qa-practice.com/object/{new_object}",
            json=body,
            headers=headers,
        )
    with allure.step('Check status code is 200'):
        assert response.status_code == 200, "Patch failed"
    with allure.step('Check body is changed'):
        assert response.json()["data"] == {"color": "red", "size": "big"}


@allure.feature('Existing object')
@allure.story('Delete an object')
@allure.title('Удалить объект')
def test_delete_an_object(before_after, new_object):

    response = requests.delete(
        f"http://objapi.course.qa-practice.com/object/{new_object}"
    )
    assert response.status_code == 200, "Delete failed"
