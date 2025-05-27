import math

MAX_BREAKPOINTS = 10_000  # Максимальное количество допустимых разрывов


def is_defined(func, x):
    """
    Проверяет, определена ли функция в точке x.
    Возвращает False, если возникает исключение или результат невалидный.
    """
    try:
        val = func(x)
        if isinstance(val, complex):
            return False
        if math.isnan(val) or math.isinf(val):
            return False
        return True
    except (ZeroDivisionError, ValueError, OverflowError, TypeError):
        return False


def get_discontinuity_points(func, a, b, n):
    """
    Ищет точки разрыва функции на отрезке [a, b] с разбиением на n частей.

    :param func: функция для анализа
    :param a: начальный предел
    :param b: конечный предел
    :param n: количество разбиений
    :return: список уникальных точек разрыва
    """
    breakpoints = set()

    # Проверка крайних точек и центра
    for point in [a, b, (a + b) / 2]:
        if not is_defined(func, point):
            breakpoints.add(round(point, 10))

    h = (b - a) / n
    for i in range(n + 1):
        point = a + i * h
        if not is_defined(func, point):
            breakpoints.add(round(point, 10))
            if len(breakpoints) >= MAX_BREAKPOINTS:
                # При слишком большом числе разрывов уменьшаем точность
                return get_discontinuity_points(func, a, b, max(n // 10, 10))

    return sorted(breakpoints)
