from config import VALID_PASSWORD, VALID_USERNAME
from ui.pages.dashboard_page import DashboardPage
from ui.pages.login_page import LoginPage
from ui.test_data.users import ERROR_TEXT, FAKE_PASSWORD, FAKE_USERNAME


class TestLogin:

    def test_valid_login(self, driver):
        """
        Проверка успешного логина
        """
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username(VALID_USERNAME)
        login_page.enter_password(VALID_PASSWORD)
        login_page.click_sign_in()

        dashboard = DashboardPage(driver)

        assert dashboard.get_user_avatar(), "Аватар не найден"
        assert dashboard.dashboard_is_visible(), "Надпись Dashboard не найдена"

    def test_failed_login(self, driver):
        """
        Проверка логина с невалидными данными
        """
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username(FAKE_USERNAME)
        login_page.enter_password(FAKE_PASSWORD)
        login_page.click_sign_in()

        assert login_page.get_error_message() == ERROR_TEXT, "Неправильный текст ошибки"
