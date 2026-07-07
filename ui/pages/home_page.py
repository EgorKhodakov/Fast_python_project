from ui.locators.home_page_locators import (HomePageLocators,
                                            ResourcesMenuLocators,
                                            SolutionsMenu)
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

    def go_to_resources_menu(self):
        """
        Нажатие на кнопку Resources в хедере
        """
        self.click(HomePageLocators.RESOURCES_BUTTON)
        self.find_element(ResourcesMenuLocators.AI)  # чтобы прогрузилось все меню

    def get_topics_elements(self):
        """
        получение списка элементов раздела Topics
        """
        elements = self.find_elements(ResourcesMenuLocators.ALL_TOPICS_LINKS)
        return [el.text for el in elements]
