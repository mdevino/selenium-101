from selenium.webdriver.common.by import By

from .base_page import BasePage
from ..elements import BaseElement, InputElement, Locator


class TrainingGroundPage(BasePage):
    url = "https://techstepacademy.com/training-ground"

    @property
    def input_field(self):
        return InputElement(self.driver, Locator(By.ID, "ipt1"))

    @property
    def button1(self):
        return BaseElement(self.driver, Locator(By.ID, "b1"))

    @property
    def button2(self):
        return BaseElement(self.driver, Locator(By.ID, "b2"))

    @property
    def another_input_field(self):
        return InputElement(self.driver, Locator(By.ID, "ipt2"))

    @property
    def button3(self):
        return BaseElement(self.driver, Locator(By.ID, "b3"))

    @property
    def button4(self):
        return BaseElement(self.driver, Locator(By.ID, "b4"))
