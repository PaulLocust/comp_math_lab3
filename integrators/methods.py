from integrators.rectangle import rectangle_left, rectangle_right, rectangle_middle
from integrators.simpson import simpson_rule
from integrators.trapezoid import trapezoid_rule

# Словарь с методами, доступными для вычислений
methods = {
    "rectangle_left": rectangle_left,
    "rectangle_right": rectangle_right,
    "rectangle_middle": rectangle_middle,
    "trapezoid": trapezoid_rule,
    "simpson": simpson_rule
}


def compute_integral(func, a, b, epsilon, method):
    """
    Функция для вычисления интеграла с помощью выбранного метода.

    :param func: функция, которую нужно интегрировать
    :param a: нижний предел интегрирования
    :param b: верхний предел интегрирования
    :param epsilon: точность вычислений
    :param method: метод для интегрирования (например, "simpson", "rectangle_left")
    :return: приближённое значение интеграла и количество разбиений
    """
    n = 4
    runge_coef = {
        "rectangle_left": 1,
        "rectangle_right": 1,
        "rectangle_middle": 3,
        "trapezoid": 3,
        "simpson": 15
    }

    coef = runge_coef.get(method)
    if coef is None:
        raise ValueError(f"Неизвестный метод: {method}")

    result = methods[method](func, a, b, n)
    error = float('inf')

    while error > epsilon:
        n *= 2
        new_result = methods[method](func, a, b, n)
        error = abs(new_result - result) / coef # Формула Рунге
        result = new_result

    return result, n