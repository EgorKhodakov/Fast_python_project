from selenium.common import TimeoutException

from ui.locators.login_page import LoginPageLocators
from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver, url="https://github.com/login"):
        super().__init__(driver, url)

    def enter_username(self, text: str) -> None:
        """
        Метод для ввода логина
        """
        self.send_keys(LoginPageLocators.USERNAME_FIELD, text)

    def enter_password(self, text: str) -> None:
        """
        Метод для ввода пароля
        """
        self.send_keys(LoginPageLocators.PASSWORD_FIELD, text)

    def click_sign_in(self) -> None:
        """
        Нажатие кнопки SIGN IN
        """
        self.click(LoginPageLocators.LOGIN_SIGN_IN)

    def get_error_message(self) -> str:
        """
        Возвращает текст ошибки
        """
        return self.get_text(LoginPageLocators.ERROR_TEXT)

    def error_container_is_visible(self) -> bool:
        """
        Проверяет наличие контейнера с ошибкой
        """
        try:
            self.find_element(LoginPageLocators.ERROR_CONTAINER)
            return True
        except TimeoutException:
            return False
