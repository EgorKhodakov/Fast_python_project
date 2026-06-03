import pytest
from test_fixture_practice.test_task_queue import TaskQueue
from test_parametrize_practice.calculator import Calculator


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