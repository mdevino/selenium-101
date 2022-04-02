from selenium.webdriver.common.by import By

from ..elements import BaseElement


class TrainingGroundPage:
    def __init__(self, driver):
        self.url = "https://techstepacademy.com/training-ground"
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    def type_into_input(self, text):
        input_element = self.driver.find_element_by_id("ipt1")
        input_element.clear()
        input_element.send_keys(text)

    def get_input_text(self):
        input_element = self.driver.find_element_by_id("ipt1")
        return input_element.get_attribute("value")

    def click_button1(self):
        button = self.driver.get_element_by_id("b1")
        button.click()

    @property
    def button1(self):
        return BaseElement(self.driver, "b1", By.ID)

    @property
    def input_field(self):
        return BaseElement(self.driver, "ipt1", By.ID)
