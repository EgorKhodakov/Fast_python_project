from ui.pages.login_page import LoginPage

class TestLogin:

    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username()
        login_page.enter_password()
        login_page.click()





