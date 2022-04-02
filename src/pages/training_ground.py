from selenium.webdriver.common.by import By

from .base_page import BasePage
from ..elements import BaseElement


class TrainingGroundPage(BasePage):
    url = "https://techstepacademy.com/training-ground"

    @property
    def button1(self):
        return BaseElement(self.driver, "b1", By.ID)

    @property
    def input_field(self):
        return BaseElement(self.driver, "ipt1", By.ID)
