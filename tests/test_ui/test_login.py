from config import VALID_PASSWORD, VALID_USERNAME, VALID_EMAIL
from ui.pages.dashboard_page import DashboardPage
from ui.pages.login_page import LoginPage
from ui.test_data.users import ERROR_TEXT
from ui.test_data.fakers import fake
import pytest


@pytest.mark.ui
class TestLogin:

    @pytest.mark.parametrize("username", (VALID_EMAIL, VALID_USERNAME))
    def test_valid_login(self, driver, username):
        """
        Проверка успешного логина
        """
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username(username)
        login_page.enter_password(VALID_PASSWORD)
        login_page.click_sign_in()

        dashboard = DashboardPage(driver)

        assert dashboard.get_user_avatar(), "Аватар не найден"
        assert dashboard.dashboard_is_visible(), "Надпись Dashboard не найдена"

    def test_failed_login(self, driver, username, password):
        """
        Проверка логина с невалидными данными
        """
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_sign_in()

        assert login_page.get_error_message() == ERROR_TEXT, "Неправильный текст ошибки"
