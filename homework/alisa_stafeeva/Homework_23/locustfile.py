from locust import task, HttpUser
import random


class ObjectUser(HttpUser):

    @task(5)
    def get_all_objects(self):
        self.client.get("/object", headers={"Content-Type": "application/json"})

    @task(1)
    def get_one_object(self):
        self.client.get(
            f"/object/{random.choice(1, 3146, 3182)}",
            headers={"Content-Type": "application/json"},
        )
