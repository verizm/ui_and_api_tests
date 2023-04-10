import random
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import selenium.common.exceptions as SE
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class UserCart:
    def __init__(self, driver):
        self.driver = driver

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


class MainForm:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.action = ActionChains(self.driver)

    _name = By.XPATH, "//input[@placeholder='First Name']"
    _last_name = (By.XPATH, "//input[@placeholder='Last Name']")
    _email = (By.XPATH, "//input[@placeholder='name@example.com']")
    _mobile = (By.XPATH, "//input[@placeholder='Mobile Number']")
    _age = (By.XPATH, "//input[@placeholder='Age']")
    _salary = (By.XPATH, "//input[@placeholder='Salary']")
    _departament = (By.XPATH, "//input[@placeholder='Department']")
    _date_of_birth = (
        By.XPATH, "//input[@id='dateOfBirthInput']")
    _address = (By.ID, "currentAddress")

    _upload_file = (By.XPATH, "//input[@id='uploadPicture']")
    _subject = (By.XPATH, "//div[contains(@class, 'subjects-auto-complete__value-container')]")
    _expand_dropdown = (By.XPATH, "//div[@id='state']// div[@class=' css-1wy0on6']")
    _dropdown = (By.CSS_SELECTOR, ".css-26l3qy-menu")
    _all_options = (By.XPATH, "//div[contains(@id,'option')]")
    _input_state = (By.CSS_SELECTOR, "#react-select-3-input")
    _input_city = (By.CSS_SELECTOR, "#react-select-4-input")

    _draggable = (By.CSS_SELECTOR, "#draggable")
    _droppable = (By.CSS_SELECTOR, "#droppable")
    _add_button = (By.CSS_SELECTOR, "#addNewRecordButton")

    def input_full_name(self, full_name: tuple):
        self.driver.find_element(*self._name).send_keys(full_name[0])
        self.driver.find_element(*self._last_name).send_keys(full_name[1])

    def set_email(self, mail: str):
        self.driver.find_element(*self._email).send_keys(mail)

    def set_mobile_phone(self, phone: str):
        self.driver.find_element(*self._mobile).send_keys(phone)

    def set_date_of_birth(self):
        elem = self.driver.find_element(*self._date_of_birth)
        self.driver.execute_script(f"arguments[0].value = '26 Feb 2023';", elem)

    def set_address(self, text):
        self.wait.until(EC.element_to_be_clickable(self._address)).send_keys(text)

    def send_file(self, file):
        self.driver.find_element(*self._upload_file).send_keys(file)

    def set_option_in_select(self, state_value, town_value):
        state = self.wait.until(EC.element_to_be_clickable(self._input_state))
        state.send_keys(state_value)
        state.send_keys(Keys.RETURN)
        town = self.wait.until(EC.element_to_be_clickable(self._input_city))
        town.send_keys(town_value)
        town.send_keys(Keys.RETURN)

    def get_text_select_option(self):
        self.driver.find_element(*self._expand_dropdown).click()
        if self.driver.find_element(self._dropdown):
            return [option.text for option in self.driver.find_element(self._all_options)]
        else:
            raise Exception("dropdown element not found")

    def set_text_in_select(self, state, town):
        element = self.driver.find_element(By.XPATH, f"//div[text()='Select State']")
        self.driver.execute_script(f"arguments[0].innerText = '{state}'", element)
        element = self.driver.find_element(By.XPATH, f"//div[text()='Select City']")
        self.driver.execute_script(f"arguments[0].innerText = '{town}'", element)

    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#submit"))).click()

    def choose_label_by_text(self, text):
        labels = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".custom-control-label")))
        for element in labels:
            try:
                if element.text == text:
                    element.click()
                    break
            except:
                raise Exception("Element not found by text")


class UserTable:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    _values_in_table = (By.XPATH, "//tbody/tr/td[2]")
    _labels_in_table = (By.XPATH, "//tbody/tr/td[1]")

    def get_lable_values(self):
        values = self.wait.until(EC.visibility_of_all_elements_located(self._values_in_table))
        return list(map(lambda x: x.text, values))






