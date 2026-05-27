import time
import random


class LoopsPractice:
    def __init__(self):
        pass

    """задание - Список чисел"""

    def list_numbers(self):
        numbers = list(range(1,8))
        for i in numbers:
            print(i)
            if i == 5:
                print(f"i = {i}, цикл завершен")
                break

    """задание  - Список строк"""
    def words_list(self):
        words = [f"str{i}" for i in range(10)]
        for word in words:
            print(word)

    """задание - Имитация нагрузки Rostics"""
    def rostics_stress(self):
        counter = 0
        while counter < 10:
            counter += 1
            stress = random.randint(1,100)
            if stress > 85:
                print(f"Предупреждение! нагрузка равна {stress}%")
            else:
                print(f"Текущая нагрузка {stress}%")
            time.sleep(0.2)





