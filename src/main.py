from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from .pages import TrainingGroundPage


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

page = TrainingGroundPage(driver)

page.go()

print(page.input_field.attribute("name"))
print(page.input_field.text)
page.input_field.enter_text("This is the first text field.")
print(page.input_field.text)

print(page.button1.text)
print(page.button1.attribute("name"))
# page.button1.click()

print(page.button2.text)
print(page.button2.attribute("name"))
# page.button2.click()

print(page.another_input_field.attribute("name"))
print(page.another_input_field.text)
page.another_input_field.enter_text("This is another text field.")
print(page.another_input_field.text)

print(page.button3.text)
print(page.button3.attribute("name"))
# page.button3.click()

print(page.button4.text)
print(page.button4.attribute("name"))
# page.button4.click()

driver.quit()
