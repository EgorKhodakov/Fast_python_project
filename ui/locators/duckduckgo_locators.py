from selenium.webdriver.common.by import By


class DuckDuckGoLocators:

    SEARCH_AREA = (By.ID, "searchbox_input")
    SEARCH_BUTTON = (By.XPATH, "//button[@aria-label = 'Поиск']")
    START_SEARCH_BUTTON = (By.XPATH, "//button/span[text() = 'Поиск']")
    SEARCH_RESULTS = (By.XPATH, "//div[@data-testid = 'web-vertical']//h2")
