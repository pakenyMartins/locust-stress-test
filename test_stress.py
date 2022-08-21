from unicodedata import name
import lorem
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task(5)
    def index(self):
        self.client.get("/", name="Home Page")

    @task(1)
    def search(self):
        self.client.post("/?s=Panquecas/"+lorem.sentence(), name="Search Page")
