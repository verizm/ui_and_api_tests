import requests
from logger import LOGGER
import json


class ApiClient:
    base_url = "https://reqres.in/api/"

    def get(self, path: str):
        responce = requests.get(url=self.base_url + path, params=None)
        if responce.ok:
            LOGGER.info(f"Get request. Status_code: {responce.raise_for_status()}, responce_body: {responce.content}")
            return json.loads(responce.content)
        else:
            LOGGER.error(f"Status_code: {responce.raise_for_status()}, responce_body: {responce.content}")

    def post(self, path: str, payload: dict):
        responce = requests.post(url=self.base_url + path, data=payload, params=None)
        if responce.ok:
            LOGGER.info(f"Post request. Status_code: {responce.raise_for_status()}, responce_body: {responce.content}")
            return json.loads(responce.content)
        else:
            LOGGER.error(f"Status_code: {responce.raise_for_status()}, responce_body: {responce.content}")
