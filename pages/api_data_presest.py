from operator import itemgetter
from pages.api_client import ApiClient
from data.data_faker import DataFaker
from pydantic import BaseModel


class UserApiData(ApiClient):

    def get_users_profile(self):
        """Return users email and password for registration"""
        user_data = []
        data = self.get("users?page=1")["data"]

        for email in map(itemgetter('email'), data):
            user_data.append({"email": email, "password": DataFaker().get_password_naitve()})
        return user_data

    def register_users(self, payload: dict):
        """Register user"""
        response = self.post("login", payload)
        return response["token"]

    def get_user_profile(self, id: str):
        return self.get("users/" + id)["data"]

    def create_user(self, obj: dict):
        return self.post("users", obj)


class User(BaseModel):
    name: str = DataFaker().get_first_name()
    job: str = DataFaker().get_job()


class UserResponce(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str


