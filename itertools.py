from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number: any) -> float:
    """Функция вычисляет квадратный корень."""
    return sqrt(number)


def calc(u_num: any) -> bool:
    """Функция проверяет введенное число."""
    if u_num <= 0:
        return
    ans = calculate_square_root(u_num)
    print(f'Мы вычислили квадратный '
          f'корень из введённого вами числа. Это будет: {ans}')


calc(25.5)
