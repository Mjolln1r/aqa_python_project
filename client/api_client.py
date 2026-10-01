import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint):
        return self.session.get(f"{self.base_url}{endpoint}")

    def post(self, endpoint, data=None):
        return self.session.post(self.base_url + endpoint, json=data)


class GetApi(APIClient):
    def get_users_id(self, users_id: int):
        return self.get(f"/users/{users_id}")


    def get_users(self):
        return self.get("/users")


class PostApi(APIClient):
    def create_post(self, data_post: dict):
        return self.post(endpoint="/posts", data=data_post)