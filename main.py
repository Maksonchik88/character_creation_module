import datetime as dt
import decimal as dc

FORMAT = '%H:%M:%S'
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}  # Словарь для хранения полученных данных.


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    return len(data) == 2 and isinstance(data[0], str) and len(data[0].split(':')) == 3 and isinstance(data[1], int) \
        and all(d.isdecimal() for d in data[0].split(':'))


def check_correct_time(time):
    """Проверка корректности параметра времени."""
    if len(storage_data) > 0 and time <= max(storage_data.keys()):
        return False
    return True


def get_step_day(steps: int):
    """Получить количество пройденных шагов за этот день."""
    all_steps = sum(storage_data.values())
    return all_steps + steps


def get_distance(steps: int):
    """Получить дистанцию пройденного пути в км."""
    return (steps * STEP_M) / 1000


def get_spent_calories(dist: float, current_time: dt.time):
    """Получить значения потраченных калорий."""
    minutes = current_time.hour * 60 + current_time.minute
    mean_speed = dist / (minutes / 60)
    spent_calories = (dc.Decimal(K_1) * dc.Decimal(WEIGHT) + (dc.Decimal(mean_speed) ** 2 / dc.Decimal(HEIGHT)) * dc.Decimal(K_2) * dc.Decimal(WEIGHT)) * dc.Decimal(minutes)
    return spent_calories
    # time = current_time.hour * 3600 + current_time.minute * 60 + current_time.second
    # spent_calories = (K_1 * WEIGHT + (((dist * 1000 / time) ** 2) / HEIGHT) * K_2 * WEIGHT) * (time / 60)
    # return spent_calories
    # В уроке «Последовательности» вы написали формулу расчета калорий.
    # Перенесите её сюда и верните результат расчётов.
    # Для расчётов вам потребуется значение времени;
    # получите его из объекта current_time;
    # переведите часы и минуты в часы, в значение типа float.


def get_achievement(dist):
    """Получить поздравления за пройденную дистанцию."""
    if dist >= 6.5:
        achievement = 'Отличный результат! Цель достигнута.'
    elif dist >= 3.9:
        achievement = 'Неплохо! День был продуктивным.'
    elif dist >= 2:
        achievement = 'Маловато, но завтра наверстаем!'
    else:
        achievement = 'Лежать тоже полезно. Главное — участие, а не победа!'
    return achievement


def show_message(dist: float, current_time: dt.time, calories: float, steps: int, achievement: str):
    print()
    print(f"Время: {current_time}.")
    print(f"Количество шагов за сегодня: {steps}.")
    print(f"Дистанция составила {dist:.2f} км.")
    print(f"Вы сожгли {calories:.2f} ккал.")
    print(achievement)
    print()


def accept_package(data):
    """Обработать пакет данных."""

    if not check_correct_data(data):
        return 'Некорректный пакет'
    pack_time = dt.datetime.strptime(data[0], FORMAT).time()
    if not check_correct_time(pack_time):
        return 'Некорректное значение времени'

    day_steps = get_step_day(data[1])
    dist = get_distance(day_steps)
    spent_calories = get_spent_calories(dist, pack_time)
    achievement = get_achievement(dist)
    show_message(dist, pack_time, spent_calories, day_steps, achievement)
    storage_data[pack_time] = data[1]
    return storage_data


package_0 = ('2:00:01', 505)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)
