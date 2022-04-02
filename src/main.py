from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from .pages import TrainingGroundPage


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

page = TrainingGroundPage(driver)

page.go()
print(page.input_field.attribute("name"))
print(page.input_field.text)
page.input_field.enter_text("Potato!")
print(page.input_field.text)
print(page.button1.text)
print(page.button1.attribute("name"))
page.button1.click()

driver.quit()
