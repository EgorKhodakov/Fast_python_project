from ui.locators.solutions_page_locators import SolutionsLocators
from ui.pages.base_page import BasePage


class CiCdPage(BasePage):
    def __init__(self, driver, url="https://github.com/solutions/use-case/ci-cd"):
        super().__init__(driver, url)

    def click_contact_sales(self):
        """
        Нажатие на кнопку "Contact sales" в верхней части страницы
        """
        self.click(SolutionsLocators.UP_CONTACT_SALES)
