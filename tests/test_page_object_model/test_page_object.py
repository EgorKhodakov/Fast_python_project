
driver = "Driver"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):

    def open(self):
        return self

    def login(self):
        return self

    def login_page_is_open(self):
        return self


def test_login_success(driver):

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login()
    assert True
