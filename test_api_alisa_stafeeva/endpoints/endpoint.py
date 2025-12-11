import allure


class Endpoint:
    url = "http://objapi.course.qa-practice.com/object"
    response = None
    json = None
    headers = {"Content-Type": "application/json"}
    object_id = None

    @allure.step("Check status code is 200")
    def check_response_status_is_corect(self):
        assert self.response.status_code == 200, "Status is incorrect"

    @allure.step("Check body is changed")
    def check_response_name_is_correct(self, name):
        assert self.response.json()["name"] == name, "Name is incorrect"

    @allure.step("Check body is changed")
    def check_response_data_is_correct(self, data):
        assert self.response.json()["data"] == data, "Data is incorrect"
