import requests
import allure
from endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):

    @allure.feature("Existing object")
    @allure.story("Put an object")
    def update_put_an_object(self, body, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f"{self.url}/{object_id}", json=body, headers=headers
        )
        return self.response

    @allure.feature("Existing object")
    @allure.story("Patch an object")
    @allure.step("Prepare test data")
    def update_patch_an_object(self, body, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f"{self.url}/{object_id}", json=body, headers=headers
        )
        return self.response
