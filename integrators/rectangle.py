def rectangle_left(func, a, b, n):
    """
    Метод левых прямоугольников для численного интегрирования.

    :param func: функция, которую нужно проинтегрировать
    :param a: нижний предел
    :param b: верхний предел
    :param n: количество разбиений
    :return: приближенное значение интеграла
    """
    h = (b - a) / n
    result = 0
    for i in range(n):
        x = a + i * h
        result += func(x)
    return result * h


def rectangle_right(func, a, b, n):
    """
    Метод правых прямоугольников для численного интегрирования.

    :param func: функция, которую нужно проинтегрировать
    :param a: нижний предел
    :param b: верхний предел
    :param n: количество разбиений
    :return: приближенное значение интеграла
    """
    h = (b - a) / n
    result = 0
    for i in range(1, n + 1):
        x = a + i * h
        result += func(x)
    return result * h


def rectangle_middle(func, a, b, n):
    """
    Метод средних прямоугольников для численного интегрирования.

    :param func: функция, которую нужно проинтегрировать
    :param a: нижний предел
    :param b: верхний предел
    :param n: количество разбиений
    :return: приближенное значение интеграла
    """
    h = (b - a) / n
    result = 0
    for i in range(n):
        x = a + (i + 0.5) * h
        result += func(x)
    return result * h