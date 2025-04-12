def rectangle_rule(func, a, b, n, mode="middle"):
    """
    Метод прямоугольников для численного интегрирования.

    :param func: функция, которую нужно проинтегрировать
    :param a: нижний предел
    :param b: верхний предел
    :param n: количество разбиений
    :param mode: способ взятия точки (left, right, middle)
    :return: приближенное значение интеграла
    """
    h = (b - a) / n
    result = 0

    if mode == "left":
        for i in range(n):
            x = a + i * h
            result += func(x)

    elif mode == "right":
        for i in range(1, n + 1):
            x = a + i * h
            result += func(x)

    elif mode == "middle":
        for i in range(n):
            x = a + (i + 0.5) * h
            result += func(x)

    else:
        raise ValueError(f"Неизвестный режим: {mode}. Используйте left, right или middle.")

    return result * h
