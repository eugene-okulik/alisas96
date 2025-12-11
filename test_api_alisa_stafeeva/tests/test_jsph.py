import pytest


TEST_DATA = [
    {"name": "alisa_object_11", "data": {"color": "red", "size": "big"}},
    {"name": "alisa_object_22", "data": {"color": "cian", "size": "small"}},
    {"name": "alisa_object_33", "data": {"color": "white", "size": "medium"}},
]


@pytest.mark.parametrize("body_value", TEST_DATA)
def test_post_an_object(start_end, before_after, body_value, create_object_endpoint):
    create_object_endpoint.new_object(body_value)
    create_object_endpoint.check_response_status_is_corect()
    create_object_endpoint.check_response_name_is_correct(body_value["name"])


def test_put_an_object(before_after, object_id, update_object_endpoint):
    update_object_endpoint.update_put_an_object(
        {"name": "alisa_object_2", "data": {"color": "red", "size": "big"}}, object_id
    )
    update_object_endpoint.check_response_status_is_corect()
    update_object_endpoint.check_response_data_is_correct(
        {"color": "red", "size": "big"}
    )


def test_patch_an_object(before_after, object_id, update_object_endpoint):
    update_object_endpoint.update_patch_an_object(
        {"data": {"color": "red", "size": "big"}}, object_id
    )
    update_object_endpoint.check_response_status_is_corect()
    update_object_endpoint.check_response_data_is_correct(
        {"color": "red", "size": "big"}
    )


def test_delete_an_object(before_after, object_id, update_object_endpoint):
    update_object_endpoint.delete_an_object(object_id)
    update_object_endpoint.check_response_status_is_corect()
