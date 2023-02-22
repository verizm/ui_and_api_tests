from faker import Faker
import string
import time
import random
import secrets
from faker.providers.phone_number.en_US import Provider as PhoneProvider
from pages.api_client import ApiClient
from faker.providers.person import Provider as PersonProvider


class DataFaker:
    def __init__(self):
        self.faker = Faker()
        self.phone_ru = PhoneProvider(self.faker)

    def get_last_name(self):
        return self.faker.last_name()

    def get_first_name(self):
        return self.faker.first_name()

    def get_address(self):
        return self.faker.address().replace("\n", " ")

    def get_email(self):
        return self.faker.email()

    def get_post_code(self):
        return self.faker.random_int(10000, 19999)

    def get_city(self):
        return self.faker.city()

    def get_password(self):
        return self.faker.password()

    def get_random_item_name(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    def get_time_for_picker(self):
        return time.strftime("%d-%m-%Y", time.localtime())

    def get_password_naitve(self):
        data = string.ascii_letters + string.digits
        return "".join(secrets.choice(data) for i in range(10))


class User(DataFaker):
    def __init__(self):
        super().__init__()
        self.name = self.get_first_name()
        self.email = self.get_email()
        self.current_address = self.get_address()
        self.permanent_address = self.get_city()


    #     }



