import pytest

from ui.pages.home_page import HomePage


@pytest.mark.ui
class TestTopicSection:

    def test_resources_menu(self, driver):
        """
        Проверка вхождения ожидаемых элементов в раздел Resources
        """
        page = HomePage(driver)
        expected_elements = {"AI", "DevOps", "Security",
                             "Software Development", "View all topics"}

        page.open()
        page.go_to_resources_menu()
        actual_elements = set(page.get_topics_elements())

        assert expected_elements.issubset(actual_elements), \
            f"Не найдены элементы {expected_elements - actual_elements}"