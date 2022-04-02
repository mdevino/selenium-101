from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement


class BaseElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element: WebElement = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(locator=self.locator)
        )
        self.web_element = element

    def click(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.locator)
        )
        element.click()

    def enter_text(self, text):
        self.web_element.send_keys(text)

    def attribute(self, attributeName):
        attribute = self.web_element.get_attribute(attributeName)
        return attribute

    @property
    def text(self):
        text = self.web_element.text
        return text
