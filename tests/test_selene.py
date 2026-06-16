import time
from selenium.webdriver.common.by import By


def test_selene(driver):
    driver.get("https://www.sports.ru/")
    time.sleep(10)
    world_cup = driver.find_element(By.XPATH, "//span[text() = 'ЧМ-26 ']")
    world_cup.click()
    assert driver.current_url == "https://www.sports.ru/football/tournament/fifa-world-cup/"


