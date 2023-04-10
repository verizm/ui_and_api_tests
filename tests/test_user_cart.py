import random
import time
from logger import LOGGER
import pytest
from data.data_faker import User
from pages.user_cart import UserCart, MainForm, UserTable


@pytest.mark.usefixtures("open_main_form")
class TestUserCart:
    @pytest.fixture(autouse=True)
    def init_page(self, create_driver):
        self.user_cart = UserCart(create_driver)
        self.form = MainForm(create_driver)
        self.user_table = UserTable(create_driver)

    def test_form(self, open_text_box_form, create_user):
        assert self.user_cart.send_form(create_user) == self.user_cart.get_labels()

    def test_main_form(self):
        self.user = User()
        self.form.input_full_name(self.user.student_name)
        self.form.set_email(self.user.email)
        self.form.choose_label_by_text(self.user.gender)
        self.form.set_mobile_phone(self.user.mobile)
        self.form.set_date_of_birth()
        self.form.choose_label_by_text(self.user.hobbies)
        self.form.set_address(self.user.address)
        self.form.set_option_in_select("NCR", "Delhi")
        self.form.click_submit()
        student_data = self.user_table.get_lable_values()
        LOGGER.info(f"Difference between {self.user.get_difference(student_data)}")
        assert self.user.matcher(student_data)





