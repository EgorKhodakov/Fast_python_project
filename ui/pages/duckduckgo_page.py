from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from ui.locators.duckduckgo_locators import DuckDuckGoLocators
from ui.pages.base_page import BasePage


class DuckDuckGoPage(BasePage):
    def __init__(self, driver, url = 'https://duckduckgo.com'):
        super().__init__(driver, url)


    def insert_in_search_box(self, text):
        """
        Заполнение поля поиска
        """
        self.send_keys(DuckDuckGoLocators.SEARCH_AREA, text)


    def start_search(self):
        """
        Нажатие на кнопку поиска
        """
        self.click(DuckDuckGoLocators.START_SEARCH_BUTTON)

    def return_search_results(self) -> int:
        """
        Возвращает количество найденных элементов на первой странице поиска
        """
        return len(self.find_elements(DuckDuckGoLocators.SEARCH_RESULTS))


