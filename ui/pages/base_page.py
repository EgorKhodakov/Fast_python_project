from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """
    Базовый класс для страниц
    принимает
    driver - экземпляр класса драйвер
    url - урл страницы
    """
    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=0.5)

    def open(self):
        """
        Метод открытия страницы
        """
        if self.url:
            self.driver.get(self.url)
        else:
            print("URL не задан")

    def find_element(self, locator: tuple[str, str]) -> WebElement:
        """
        Нахождение видимого элемента
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: tuple[str, str]) -> None:
        """
        Клик по элементу
        """
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator: tuple[str, str], text: str) -> None:
        """
        Вставка текста в элемент
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_current_url(self) -> str:
        """
        Возвращает текущий урл
        """
        return self.driver.current_url

    def get_text(self, locator: tuple[str, str]) -> str:
        return self.find_element(locator).text


    def get_attribute(self, locator: tuple[str, str], attribute: str) -> str:
        """
        возвращает параметр аттрибута
        """
        return self.find_element(locator).get_property(attribute)
