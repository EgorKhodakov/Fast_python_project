"""Создание класса и вызов метода с выводм всех полей"""


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print_car_info(self):
        print(f"{self.brand} {self.model} {self.year}")


volvo = Car("Volvo", "S560", 2000)
kia = Car("Kia", "carnival", 2019)
ford = Car("Ford", "focus", 2010)
volvo.print_car_info()
kia.print_car_info()
ford.print_car_info()


"""Создание функции для определения дня недели"""

data = {
    1: "sunday",
    2: "monday",
    3: "tuesday",
    4: "wednesday",
    5: "thursday",
    6: "friday",
    7: "saturday",
}


def week_day() -> None:
    day = int(input("please enter day in 1-7 - "))
    while day not in range(1, 8):
        day = int(input("please enter day in 1-7 - "))
    print(f"today is {data[day]}")


week_day()


"""Создание списка от 1-9 и нахождение максимума с помощью цикла for"""

numbers = [i for i in range(1, 9)]
max_number = 0

for i in numbers:
    if max_number < i:
        max_number = i

print(f"Максимальное число из списка - {max_number}")

"""Функция принимающая список строк и возвращающая те, чья длинна больше 5"""


def list_function(list1: list) -> list:
    list2 = []
    for i in list1:
        if len(i) >= 5:
            list2.append(i)
    return list2


"""Создание класса Lead"""


class Lead:
    def __init__(self, name):
        self.name = name


def change_lead_name(lead_obj, new_name: str) -> None:
    lead_obj.name = new_name


lead = Lead("Egor")
print(f"Начальное имя лида {lead.name}")

change_lead_name(lead, "Alexander")

print(f"Измененное имя лида {lead.name}")

"""Создание класса Student, его экземпляров и вывод среднего бала"""


class Student:
    def __init__(self, name, age, grade: list[float]) -> None:
        self.name = name
        self.age = age
        self.grade = grade


def get_avg_grade(student: Student) -> float:
    return round(sum(student.grade) / len(student.grade), 1)


def age_name(student: Student):
    print(f"Студенту {student.name} {student.age} лет")


Egor = Student("Egor", 45, [1.5, 5.5, 3.6])
Ivan = Student("Ivan", 45, [6.5, 2.8, 4.9])
Alina = Student("Alinna", 45, [3.3, 2.1, 2.8])

print(get_avg_grade(Egor))
print(get_avg_grade(Ivan))
print(get_avg_grade(Alina))

"""Создание списка students и вывод имени студента со средним балом > 4.1"""

student_list = [Egor, Ivan, Alina]

for i in student_list:
    if get_avg_grade(i) > 4.1:
        print(f"{i.name} имеет средний бал {get_avg_grade(i)}")
