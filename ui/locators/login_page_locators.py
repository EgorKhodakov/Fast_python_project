from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_FIELD = (By.ID, "login_field")
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[type="password"]')
    LOGIN_SIGN_IN = (By.CSS_SELECTOR, '[value="Sign in"]')
    ERROR_TEXT = (By.CLASS_NAME, "js-flash-alert")
    ERROR_CONTAINER = (By.CSS_SELECTOR, "#js-flash-container > div")
