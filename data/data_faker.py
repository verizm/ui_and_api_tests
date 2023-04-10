from faker import Faker
import string
import time
import random
import secrets
from dataclasses import dataclass
from faker.providers.phone_number.en_US import Provider as PhoneProvider


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

    def get_mobile_phone(self):
        return ''.join(str(random.randint(0, 9)) for _ in range(10))

    def get_email(self):
        return self.faker.email()

    def get_post_code(self):
        return self.faker.random_int(10000, 19999)

    def get_city(self):
        return self.faker.city()

    def get_password(self):
        return self.faker.password()

    def get_job(self):
        return self.faker.job()

    def get_random_item_name(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    def get_time_for_picker(self):
        return time.strftime("%d-%b-%Y", time.localtime())

    def get_time_for_table(self):
        return time.strftime("%d %B,%Y", time.localtime())

    def get_password_naitve(self):
        data = string.ascii_letters + string.digits
        return "".join(secrets.choice(data) for i in range(10))


@dataclass
class User(DataFaker):
    student_name: tuple = DataFaker().get_first_name(), DataFaker().get_last_name()
    email: str = DataFaker().get_email()
    gender: str = random.choice(['Male', 'Female', 'Other'])
    mobile: str = DataFaker().get_mobile_phone()
    date_of_birth: str = DataFaker().get_time_for_table()
    subjects: str = ''
    hobbies: str = random.choice(['Sport', 'Reading', 'Music'])
    picture: str = ''
    address: str = DataFaker().get_address()
    state_city: str = 'NCR Delhi'

    def get_difference(self, data):
        user_obj = list(self.__dict__.values())
        user_obj[0], user_obj[4] = " ".join(user_obj[0]), DataFaker().get_time_for_table()
        difference = list((elem[0], elem[1]) for elem in zip(user_obj, data) if elem[0] != elem[1])
        return difference

    def matcher(self, data):
        return False if self.get_difference(data) else True


class UserEx(DataFaker):
    def __init__(self):
        super().__init__()
        self.name = self.get_first_name()
        self.email = self.get_email()
        self.current_address = self.get_address()
        self.permanent_address = self.get_city()

    #     }
