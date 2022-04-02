from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from .pages import TrialPage


options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("--hide-scrollbars")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

page = TrialPage(driver)


def go_to_page():
    print("Going to trials page...")
    page.go()
    driver.save_screenshot("00-page-arrival.png")


def solve_stone_riddle():
    print("Solving stone challenge...")

    page.stone_riddle_input.enter_text("rock")
    page.stone_riddle_answer_button.click()

    driver.save_screenshot("01-stone-riddle-pass.png")


def solve_secrets_riddle():
    print("Solving secrets challenge...")
    stone_riddle_answer = page.stone_riddle_answer.text

    page.secrets_riddle_input.enter_text(stone_riddle_answer)
    page.secrets_riddle_answer_button.click()

    driver.save_screenshot("02-secrets-riddle-pass.png")


def solve_merchants_riddle():
    print("Solving merchants riddle...")

    richest_merchant_name = page.get_richest_merchant()
    page.merchants_riddle_input.enter_text(richest_merchant_name)
    page.merchants_riddle_answer_button.click()

    driver.save_screenshot("03-merchants-riddle-pass.png")


def check_answers():
    print("Checking answers...")

    page.check_answers_button.click()

    assert page.trial_complete_banner.text == "Trial Complete"

    driver.save_screenshot("04-answers-check.png")


if __name__ == "__main__":
    go_to_page()
    solve_stone_riddle()
    solve_secrets_riddle()
    solve_merchants_riddle()
    check_answers()
