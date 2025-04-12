MAX_BREAKPOINTS = 10_000  # Максимальное количество разрывов для поиска


def get_discontinuity_points(func, a, b, n):
    """
    Функция для поиска точек разрывов на интервале [a, b].
    Если функция вызывает ошибку (например, деление на ноль), то эта точка считается точкой разрыва.

    :param func: функция, которую нужно проверить
    :param a: нижний предел
    :param b: верхний предел
    :param n: количество разбиений интервала для проверки
    :return: список точек разрыва
    """
    breakpoints = []

    # Проверка крайних точек интервала
    try:
        func(a)
    except (ZeroDivisionError, OverflowError, ValueError):
        breakpoints.append(a)

    try:
        func(b)
    except (ZeroDivisionError, OverflowError, ValueError):
        breakpoints.append(b)

    # Проверка середины интервала
    try:
        func((a + b) / 2)
    except (ZeroDivisionError, OverflowError, ValueError):
        breakpoints.append((a + b) / 2)

    # Разбиение интервала на n частей и проверка каждой точки
    h = (b - a) / n
    for i in range(n):
        point = a + i * h
        try:
            func(point)
        except (ZeroDivisionError, OverflowError, ValueError):
            breakpoints.append(point)
            if len(breakpoints) >= MAX_BREAKPOINTS:
                # Если слишком много разрывов, уменьшаем шаг и продолжаем поиск
                return get_discontinuity_points(func, a, b, n // 10)

    return list(set(breakpoints))  # Убираем дубликаты, если они есть

