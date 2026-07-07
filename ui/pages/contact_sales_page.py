from ui.locators.enterprise_page_locators import EnterpriseLocators
from ui.pages.base_page import BasePage


class EnterprisePage(BasePage):
    def __init__(self, driver, url="https://github.com/enterprise/"):
        super().__init__(driver, url)

    def insert_name(self, text):
        """
        Заполнение поля First name
        """
        self.send_keys(EnterpriseLocators.FIRST_NAME, text)

    def insert_last_name(self, text):
        """
        Заполнение поля Last name
        """
        self.send_keys(EnterpriseLocators.LAST_NAME, text)

    def insert_company(self, text):
        """
        Заполнение поля Company
        """
        self.send_keys(EnterpriseLocators.COMPANY, text)

    def insert_job_title(self, text):
        """
        Заполнение поля Job title
        """
        self.send_keys(EnterpriseLocators.JOB_TITE, text)

    def insert_email(self, email):
        """
        Заполнение поля Work email
        """
        self.send_keys(EnterpriseLocators.WORK_EMAIL, email)

    def get_first_name(self):
        """
        Возвращает введенное в поле First name значение
        """
        return self.get_attribute(EnterpriseLocators.FIRST_NAME, "value")

    def get_last_name(self):
        """
        Возвращает введенное в поле Last name значение
        """
        return self.get_attribute(EnterpriseLocators.LAST_NAME, "value")

    def get_company_name(self):
        """
        Возвращает введенное в поле Company name значение
        """
        return self.get_attribute(EnterpriseLocators.COMPANY, "value")
