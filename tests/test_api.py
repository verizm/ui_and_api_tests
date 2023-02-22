import pytest
from pages.api_data_presest import UserApiData

data_users = UserApiData()


@pytest.mark.parametrize("register", data_users.get_users_profile(), indirect=True,
                         ids=[i for i in range(len(data_users.get_users_profile()))])
def test_login(register):
    profile, token = register
    assert token == data_users.register_users(profile)
