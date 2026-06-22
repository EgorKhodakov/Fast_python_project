from selenium.webdriver.common.by import By


class DashboardLocators:
    USER_AVATAR = (By.CSS_SELECTOR, "[data-component = 'Avatar']")
    DASHBOARD = (By.XPATH, "//span[text() = 'Dashboard']")
