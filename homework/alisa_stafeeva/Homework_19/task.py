import requests


def clear(post_id):
    return requests.delete(f"http://objapi.course.qa-practice.com/object/{post_id}")


def post_a_post():
    body = {"name": "alisa_object_1", "data": {"color": "red", "size": "big"}}
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        "http://objapi.course.qa-practice.com/object", json=body, headers=headers
    )
    assert response.status_code == 201, "Status is incorrect"
    assert response.json()["id"] == 581, "Id is incorrect"
    clear(response.json()["id"])


def new_post():
    body = {"name": "alisa_object_2", "data": {"color": "black", "size": "giant"}}
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        "http://objapi.course.qa-practice.com/object", json=body, headers=headers
    )
    return response.json()["id"]


def put_a_post():
    post_id = new_post()
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


def patch_a_post():
    post_id = new_post()
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


def delete_a_post():
    post_id = new_post()
    response = requests.delete(f"http://objapi.course.qa-practice.com/object/{post_id}")
    assert response.status_code == 204, "Delete failed"
