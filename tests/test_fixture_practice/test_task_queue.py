import uuid
from datetime import datetime
from typing import Optional, List
import pytest


class Task:
    """Класс задачи."""

    def __init__(self, name: str, priority: int = 5):
        self.id = str(uuid.uuid4())[:8]
        self.name = name
        self.priority = priority  # 1 - высший, 10 - низший
        self.created_at = datetime.now()
        self.completed = False

    def mark_completed(self):
        self.completed = True


class TaskQueue:
    """Простая очередь задач."""

    def __init__(self):
        self._tasks: List[Task] = []
        self._log: List[str] = []

    def add_task(self, name: str, priority: int = 5) -> str:
        """Добавить задачу в очередь. Возвращает ID задачи."""
        task = Task(name, priority)
        self._tasks.append(task)
        self._log.append(f"ADD: {task.id} - {name} (priority {priority})")
        return task.id

    def get_next_task(self) -> Optional[Task]:
        """Получить следующую задачу (с наивысшим приоритетом)."""
        if not self._tasks:
            return None

        # Сортируем по приоритету (меньше число = выше приоритет)
        self._tasks.sort(key=lambda t: t.priority)
        return self._tasks[0]

    def complete_task(self, task_id: str) -> bool:
        """Отметить задачу выполненной. Возвращает True если задача найдена."""
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                task.mark_completed()
                self._tasks.pop(i)
                self._log.append(f"DONE: {task_id}")
                return True
        return False

    def get_pending_count(self) -> int:
        """Количество невыполненных задач."""
        return len(self._tasks)

    def get_log(self) -> List[str]:
        """Получить лог операций."""
        return self._log.copy()

    def clear(self):
        """Очистить очередь."""
        self._tasks.clear()
        self._log.clear()


"""Проверка фикстуры с видимостью scope=module и yield находящейся в conftest"""


def test_is_ywo(module_queue: TaskQueue):
    assert module_queue.get_pending_count() == 2


def test_add_task(module_queue: TaskQueue):
    module_queue.add_task("retro")
    assert module_queue.get_pending_count() == 3


def test_len_tests_is_three(module_queue: TaskQueue):
    assert module_queue.get_pending_count() == 3


"""Проверка фикстуры с видимостью autouse=True"""


@pytest.fixture(autouse=True)
def log_operations(request):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"запущен тест {request.node.name}\n")


def test_add_task_with_autouse_fixture(module_queue: TaskQueue):
    module_queue.add_task("dayli")
    assert module_queue.get_pending_count() == 4


def test_get_next_task(module_queue: TaskQueue):
    assert module_queue.get_next_task() is not None
