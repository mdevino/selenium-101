from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get("https://www.google.com")
driver.get("https://techstepacademy.com/training-ground")

print(driver.title)

driver.quit()
