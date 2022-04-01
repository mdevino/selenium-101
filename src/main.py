from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from .pages import TrainingGroundPage


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

page = TrainingGroundPage(driver)

page.go()
page.type_into_input("Yo!")
text = page.get_input_text()

print(f"Text: '{text}'")

driver.quit()
