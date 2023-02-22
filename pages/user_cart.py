import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import selenium.common.exceptions as SE
from selenium.webdriver.support.wait import WebDriverWait


class UserCart:
    def __init__(self, driver):
        self.driver = driver


    class UserCartLocators:
        pass

    def get_page(self, url):
        self.driver.get(url)

    def send_form(self, user_obj):
        """Input test data into form of cart-user"""
        self.driver.find_element(By.XPATH, "//input[@placeholder='Full Name']").send_keys(user_obj.name)
        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys(user_obj.email)
        self.driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys(user_obj.current_address)
        self.driver.find_element(By.XPATH, '//textarea[@id="permanentAddress"]').send_keys(user_obj.permanent_address)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        return [user_obj.name, user_obj.email,
                user_obj.current_address, user_obj.permanent_address]

    def get_labels(self):
        """Get labels text after submit the form"""
        labels = self.driver.find_elements(By.CSS_SELECTOR, ".border p")
        return [element.text.split(":")[1] for element in labels]
