from selenium.webdriver.common.by import By

from .base_page import BasePage
from ..elements import InputElement, BaseElement
from ..elements.locator import Locator


class TrialPage(BasePage):
    url = "https://techstepacademy.com/trial-of-the-stones"

    @property
    def stone_riddle_input(self):
        return InputElement(self.driver, Locator(By.ID, "r1Input"))

    @property
    def stone_riddle_answer_button(self):
        return BaseElement(self.driver, Locator(By.ID, "r1Btn"))

    @property
    def stone_riddle_answer(self):
        return BaseElement(
            self.driver, Locator(By.XPATH, "//div[@id='passwordBanner']/h4")
        )

    @property
    def secrets_riddle_input(self):
        return InputElement(self.driver, Locator(By.ID, "r2Input"))

    @property
    def secrets_riddle_answer_button(self):
        return BaseElement(self.driver, Locator(By.ID, "r2Butn"))

    @property
    def secrets_riddle_answer(self):
        return BaseElement(
            self.driver, Locator(By.XPATH, "//div[@id='successBanner1']/h4")
        )

    @property
    def merchants_riddle_input(self):
        return InputElement(self.driver, Locator(By.ID, "r3Input"))

    @property
    def merchants_riddle_answer_button(self):
        return BaseElement(self.driver, Locator(By.ID, "r3Butn"))

    @property
    def check_answers_button(self):
        return BaseElement(self.driver, Locator(By.ID, "checkButn"))

    @property
    def trial_complete_banner(self):
        return BaseElement(
            self.driver, Locator(By.XPATH, "//div[@id='trialCompleteBanner']/h4")
        )

    def get_richest_merchant(self):
        merchant_divs = self.driver.find_elements(By.XPATH, "//div/span/..")
        merchants = []
        for div in merchant_divs:
            name = div.find_element(By.XPATH, ".//span/b").text
            wealth = int(div.find_element(By.XPATH, ".//p").text)
            merchants.append((name, wealth))

        return self._get_richest_merchant_name(merchants)

    def _get_richest_merchant_name(self, merchants: list):
        merchants.sort(key=lambda x: x[1], reverse=True)
        return merchants[0][0]
