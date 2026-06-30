from ui.pages.duckduckgo_page import DuckDuckGoPage
import pytest


@pytest.mark.ui
class TestSearchPage:

    @pytest.mark.xfail(reason="Тесты падают в headless режиме.")
    @pytest.mark.parametrize('text', ("qa", "aqa", "python"))
    def test_return_search_results(self, driver, text):
        page = DuckDuckGoPage(driver)

        page.open()
        page.insert_in_search_box(text)
        page.start_search()

        assert page.return_search_results() >= 5

