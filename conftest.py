import pytest
from test_fixture_practice.test_task_queue import TaskQueue

@pytest.fixture(scope="module")
def module_queue():
    print("СОЗДАЮ очередь (один раз для всех тестов)")
    task_queue = TaskQueue()
    task_queue.add_task("sprint")
    task_queue.add_task("backlog")
    yield task_queue
    task_queue.clear()