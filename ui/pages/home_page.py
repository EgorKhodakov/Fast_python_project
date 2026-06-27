from ui.locators.home_page_locators import HomePageLocators, SolutionsMenu
from ui.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver, url="https://github.com/"):
        super().__init__(driver, url)

    def go_to_solution_menu(self):
        """
        Нажатие на кнопку SolutionsMenu в хедере
        """
        self.click(HomePageLocators.SOLUTIONS_BUTTON)

    def select_cicd(self):
        """
        Нажатие на кнопку CI/CD в меню Solutions
        """
        self.click(SolutionsMenu.CI_CD)
