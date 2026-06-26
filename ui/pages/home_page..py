from ui.locators.home_page_locators import HomePageLocators, SolutionsMenu
from ui.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver, url="https://github.com/"):
        super().__init__(driver, url)


    def click_on_solution_menu(self):
        self.click(HomePageLocators.SOLUTIONS_BUTTON)


    def click_on_ci_cd(self):
        self.click(SolutionsMenu.CI_CD)



        











