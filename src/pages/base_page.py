from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)
