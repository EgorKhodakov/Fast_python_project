import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from tests.test_fixture_practice.test_task_queue import TaskQueue
from tests.test_parametrize_practice.calculator import Calculator


@pytest.fixture(scope="module")
def module_queue():
    print("СОЗДАЮ очередь (один раз для всех тестов)")
    task_queue = TaskQueue()
    task_queue.add_task("sprint")
    task_queue.add_task("backlog")
    yield task_queue
    task_queue.clear()


@pytest.fixture(scope="module")
def calk():
    calk = Calculator()
    return calk


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    #driver.maximize_window()
    yield driver
    driver.quit()
