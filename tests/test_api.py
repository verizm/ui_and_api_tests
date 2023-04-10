import json
import pytest
from jsonschema import validate
from pydantic import BaseModel, ValidationError
from pages.api_data_presest import (User, UserResponce)
from pages.api_data_presest import UserApiData

data_users = UserApiData()


@pytest.mark.parametrize("register", data_users.get_users_profile(), indirect=True,
                         ids=[i for i in range(len(data_users.get_users_profile()))])
def test_login(register):
    profile, token = register
    assert token == data_users.register_users(profile)


def test_create_user(schema):
    payload = dict(User())
    responce = UserApiData().create_user(payload)
    body = json.loads(responce.content)
    try:
        UserResponce.parse_raw(responce.content)
    except ValidationError as e:
        print(e.json())

    assert responce.status_code == 201
    assert body['name'] == payload['name']



