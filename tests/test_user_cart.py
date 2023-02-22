import pytest

from pages.user_cart import UserCart


class TestUserCart:
    @pytest.fixture(autouse=True)
    def init_page(self, create_driver):
        self.user_cart = UserCart(create_driver)

    def test_form(self, open_text_box_form, create_user):
        print(self.user_cart.send_form(create_user))
        print(self.user_cart.get_labels())
        assert self.user_cart.send_form(create_user) == self.user_cart.get_labels()

