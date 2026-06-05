import pytest
from tests.test_fixture_practice import TaskQueue
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


@pytest.fixture(scope="module")
def driver():
    return "Driver"