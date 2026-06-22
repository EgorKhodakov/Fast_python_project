from selenium.common import TimeoutException

from ui.locators.dashboard_page import DashboardLocators
from ui.pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, driver, url=None):
        super().__init__(driver, url)

    def get_user_avatar(self) -> bool:
        """
        Проверка, что пользователь авторизован и аватар виден
        """
        try:
            self.find_element(DashboardLocators.USER_AVATAR)
            return True
        except TimeoutException:
            return False

    def dashboard_is_visible(self) -> bool:
        """
        Проверка, что надпись Dashboard видна на странице
        """
        try:

            self.find_element(DashboardLocators.DASHBOARD)
            return True
        except TimeoutException:
            return False
