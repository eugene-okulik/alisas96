import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):
    @allure.feature("Existing object")
    @allure.story("Delete an object")
    @allure.title("Удалить объект")
    def delete_an_object(self, object_id):
        self.response = requests.delete(f"{self.url}/{object_id}")
        return self.response
