import requests


def clear(post_id):
    return requests.delete(f"http://objapi.course.qa-practice.com/object/{post_id}")


def post_an_object():
    body = {"name": "alisa_object_1", "data": {"color": "red", "size": "big"}}
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        "http://objapi.course.qa-practice.com/object", json=body, headers=headers
    )
    assert response.status_code == 200, "Status is incorrect"
    assert response.json()["name"] == "alisa_object_1", "Name is incorrect"
    clear(response.json()["id"])


def new_object():
    body = {"name": "alisa_object_2", "data": {"color": "black", "size": "giant"}}
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        "http://objapi.course.qa-practice.com/object", json=body, headers=headers
    )
    return response.json()["id"]


def put_an_object():
    post_id = new_object()
    body = {"name": "alisa_object_2", "data": {"color": "red", "size": "big"}}
    headers = {"Content-Type": "application/json"}
    response = requests.put(
        f"http://objapi.course.qa-practice.com/object/{post_id}",
        json=body,
        headers=headers,
    )
    assert response.status_code == 200, "Put failed"
    assert response.json()["data"] == {"color": "red", "size": "big"}
    clear(post_id)


def patch_an_object():
    post_id = new_object()
    body = {"data": {"color": "red", "size": "big"}}
    headers = {"Content-Type": "application/json"}
    response = requests.patch(
        f"http://objapi.course.qa-practice.com/object/{post_id}",
        json=body,
        headers=headers,
    )
    assert response.status_code == 200, "Patch failed"
    assert response.json()["data"] == {"color": "red", "size": "big"}
    clear(post_id)


def delete_an_object():
    post_id = new_object()
    response = requests.delete(f"http://objapi.course.qa-practice.com/object/{post_id}")
    assert response.status_code == 200, "Delete failed"
