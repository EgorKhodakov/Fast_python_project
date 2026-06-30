from ui.pages.home_page import HomePage
from ui.pages.contact_sales_page import EnterprisePage
from ui.pages.cicd_page import CiCdPage
from ui.test_data.fakers import fake
import pytest


@pytest.mark.ui
class TestEnterprisePage:

    def test_contact_sales_form(self, driver):
        """
        Проверка соответствия заполняемых полей
        """
        # Фейковые данные для заполнения полей
        name = fake.first_name()
        last_name = fake.last_name()
        company_name = fake.company()

        # Открываем домашнюю страницу
        home_page = HomePage(driver)

        home_page.open()
        home_page.go_to_solution_menu()
        home_page.select_cicd()

        # Открываем страницу solutions
        cicd_page = CiCdPage(driver)

        cicd_page.click_contact_sales()

        # Открываем страницу Enterprise
        enterprise_page = EnterprisePage(driver)

        enterprise_page.insert_name(name)
        enterprise_page.insert_last_name(last_name)
        enterprise_page.insert_company(company_name)

        # Проверяем соответствия введенных значений.
        assert enterprise_page.get_first_name() == name
        assert enterprise_page.get_last_name() == last_name
        assert enterprise_page.get_company_name() == company_name
