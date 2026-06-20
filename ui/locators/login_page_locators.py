from selenium.webdriver.common.by import By

#SIGN_IN = (By.XPATH, "//a[contains(text(), 'Sign in')]")
USERNAME_FIELD = (By.ID, "login_field")
PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[type="password"]')
LOGIN_SIGN_IN = (By.CSS_SELECTOR, '[value="Sign in"]')